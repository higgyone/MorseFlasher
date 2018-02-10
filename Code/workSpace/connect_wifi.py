import network
import id_key

def connect():
  
  print("*****Starting connection*****")
  
  ssid = id_key.network_id
  key = id_key.network_key
  
  station = network.WLAN(network.STA_IF)
  
  if station.isconnected() == True:
    print("*****Already connected*****")
    return
     
  station.active(True)
  station.connect(ssid, key)
  
  while station.isconnected() == False:
    pass
    
  print("*****Connection successful*****")
  print(station.ifconfig())
  
  
  

