import webmorse
from morseThread import MorseThread as mt

def startup():
  """Automatically connect to the wifi"""
  webmorse.run_server()
  
def main_loop():
  """main loop"""
  
  while True:
    """Add loop code here"""
    


startup()
main_loop()

