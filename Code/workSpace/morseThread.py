from machine import Pin
import morseTranslate as mt
import time
import _thread

class MorseThread:    
  def __init__(self):    
    self.led=Pin(21,Pin.OUT)    
    self.morse_string = "c"

  def update_morse(self,data):
    self.morse_string = data
    
  def run_morse_thread(self):
    _thread.start_new_thread(self.morse_writer, ())
      
  def morse_writer(self):
    while True:
      mc = None
      ma = None
      for mc in self.morse_string:
        ma = mt.get_morse_char(mc)
        
        for j in ma:
          self.led.value(0)
          time.sleep(0.5)
          self.led.value(1)
          if j:
            time.sleep(1)
          else:
            time.sleep(0.5)




