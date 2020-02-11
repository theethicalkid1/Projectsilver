import webbot
import os
import time
import random
from getkey import *
os.system('pip3 install pyautogui')
driver = webbot.Browser()
driver.go_to('google.com')

while True: 
  key = getkey()
  if key == '@':
    driver.type("@")
