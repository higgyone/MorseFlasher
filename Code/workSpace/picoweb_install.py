import upip
import connect_wifi
import os

"""Install picoweb on ESP32"""

def install():  
  """Install picoweb"""
  
  if 'lib' in os.listdir():
    if 'picoweb' in os.listdir('lib'):
      print("picoweb already installed")
      return
     
  if connect_wifi.is_connected():    
    print("Installing picoweb")    
    upip.install('picoweb')  
  else:    
    print("Network not connected, picoweb not installed")





