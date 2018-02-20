import network
import os
import socket
import gc
import id_key
import morseTranslate
import time
from morseThread import MorseThread as mt


SSID=id_key.network_id               #set the wifi ID
PASSWORD=id_key.network_key          #set the wifi password
wlan=None
s=None

def connectWifi(ssid,passwd): 
  global wlan
  wlan=network.WLAN(network.STA_IF)      #create a wlan object 
  wlan.active(True)                                   #Activate the network interface 
  wlan.disconnect()                                   #Disconnect the last connected WiFi
 
  wlan.connect(ssid,passwd)                           #connect wifi
  
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    
    time.sleep(1)
  
  return True



def ajaxWebserv():
  # minimal Ajax in Control Webserver
  
  global s
  
  morse = mt()
  morse.run_morse_thread()
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create stream socket
  
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #Set the value of the given socket option
  
  s.bind((wlan.ifconfig()[0], 80))                      #bind ip and port
  
  s.listen(1)                                           #listen message   ???
  
  while True:
    
    conn, addr = s.accept()                             #Accept a connection,conn is a new socket object
    
    #print("Got a connection from %s" % str(addr))
    
    request = conn.recv(1024)                           #Receive 1024 byte of data from the socket
    
    conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: ESP32\nContent-Type: text/html\n\n')
   
    request = str(request)
    
    ib = request.find('user_morse=')                           #find the string 'Val=' from request
    
    print(ib)
    
    
    if ib > 0 :
      
      ie = request.find(' ', ib)                        #init address of the index with ib,then find ' '                         
        
      
      Val = request[ib+11:ie]                           #get the string of ib+11 to ie in the request

                                                        # i.e.'user_morse=' is 11 in length
      
      if len(Val) > 32:
        
        Val = Val[:32]
      
      

      if not morseTranslate.validate_input(Val):
        
        print("Invalid input")
        
        Val = "Invalid " + Val
        
      else:
        morse.update_morse(Val)
      
      
      print("Val =", Val)
      
      conn.send(Val)                                    #send data back
    
    with open('form.html', 'r') as html:            #open file 'webCtrl.htm' with readonly
      
      conn.sendall(html.read())                       #read data from 'webCtrl.htm',and send all of the data
    
    conn.sendall('\r\n')
    
    conn.close()                                        #close file 
    #print("Connection wth %s closed" % str(addr))



def run_server():
  
  #Catch exceptions,stop program if interrupted accidentally in the 'try'
  
  try:
    
    connectWifi(SSID, PASSWORD)
    
    ajaxWebserv()
  
  except:
    
    if (s):
      
      s.close()
      
    
    wlan.disconnect()
    
    wlan.active(False)
