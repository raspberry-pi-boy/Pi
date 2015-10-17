from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()


while True:
    lcd.begin(16, 1)
    
    lcd.message("3.14159265358979\n3238462643383279")
    
    sleep (10)
    
    lcd.clear()
    
    lcd.message("50288419716939937\n5105820974944592")

    sleep (10)
