from machine import Pin,PWM
import network
import os
import time
import socket
import gc
import id_key

SSID=id_key.network_id                                         #set the wifi ID 
PASSWORD=id_key.network_key                                 #set the wifi password
wlan=None
s=None
led=None

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)                     #create a wlan object
  wlan.active(True)                                     #Activate the network interface
  wlan.disconnect()                                     #Disconnect the last connected WiFi
  wlan.connect(ssid,passwd)                             #connect wifi
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True
def ajaxWebserv():
  # minimal Ajax in Control Webserver
  global s,led
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create stream socket
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #Set the value of the given socket option
  s.bind((wlan.ifconfig()[0], 80))                      #bind ip and port
  s.listen(1)                                           #listen message   ???
  while True:
    conn, addr = s.accept()                             #Accept a connection,conn is a new socket object
    #print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)                           #Receive 1024 byte of data from the socket
    conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: FireBeetle\nContent-Type: text/html\n\n')

    request = str(request)
    ib = request.find('Val=')                           #find the string 'Val=' from request
    if ib > 0 :
      ie = request.find(' ', ib)                        #init address of the index with ib,then find ' '
      Val = request[ib+4:ie]                            #get the string of ib+4 to ie in the request
      print("Val =", Val)
      led.duty(int(Val)*100)                            #set the duty of led
      conn.send(Val)                                    #send data
    else:
      with open('webCtrl.htm', 'r') as html:            #open file 'webCtrl.htm' with readonly
        conn.sendall(html.read())                       #read data from 'webCtrl.htm',and send all of the data
    conn.sendall('\r\n')
    conn.close()                                        #close file 
    #print("Connection wth %s closed" % str(addr))

#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
  led=PWM(Pin(2),freq=100)                              #create led object
  led.init()
  led.duty(0)
  connectWifi(SSID, PASSWORD)
  ajaxWebserv()
except:
  if (s):
    s.close()
  led.deinit()
  wlan.disconnect()
  wlan.active(False)







