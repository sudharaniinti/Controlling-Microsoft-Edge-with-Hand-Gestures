import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui
pyautogui.FAILSAFE = False
ArduinoSerial = serial.Serial('com3',9600) #Create Serial port object called arduinoSerial
time.sleep(2) #wait for 2 seconds for the communication to get established
while 1:
  incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
  print (incoming)
  if 'Up' in incoming:
    pyautogui.hotkey('shift', 'space')
  if 'Down' in incoming:
    pyautogui.typewrite(['space'], 0.2)
  if 'Zoom_in' in incoming:
    pyautogui.hotkey('ctrl', '+')
  if 'Zoom_out' in incoming:
    pyautogui.hotkey('ctrl', '-')
  if 'Open' in incoming:
    pyautogui.hotkey('win', '1')
  if 'Close' in incoming:
    pyautogui.click(x=1919, y=0)  # move to 1919,0 then click the left mouse button.
  incoming = "";
