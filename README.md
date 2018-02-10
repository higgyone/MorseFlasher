# MorseFlasher
Harware design and code for a morse code warning light flasher using a ESP32 for web control 
Code is written using uPyCraft IDE (https://github.com/DFRobot/uPyCraft)
Dev board is ESP32-DevKitC(ESP32_Core_Board_V2)


# Notes
* Use uPyCraft IDE to do the download of uPython and IDE:
https://techtutorialsx.com/2017/07/20/esp32-micropython-getting-started-with-the-upycraft-ide/

* If no COM port when plugged in need to download and install CP210x_Universal_Windows_Driver from SiLabs to talk to it:
https://www.silabs.com/products/interface/usb-bridges/classic-usb-bridges/device.cp2102

* uPyCraft will upload micropython to board
This didnt work
install micro python on ESP32
https://diyprojects.io/reinstall-micropython-firmware-esp8266-esp32-esptool-py-script/#.Wnoh9Ux2tEY

* Hello world on uPyCraft:
https://dfrobot.gitbooks.io/upycraft/content/helloworld.html

* Getting started with ESP32 dev kit:
http://esp-idf.readthedocs.io/en/latest/get-started/get-started-devkitc.html

* Need a main.py to stop OSError: [Errno 2] ENOENT

* Getting picoweb:
  connect to WiFi as network.STA_IF
  then:
  ```
  import upip
  upip.install('picoweb')
  ```
