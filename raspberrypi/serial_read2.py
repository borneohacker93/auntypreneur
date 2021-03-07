import time
import requests
import serial
import os
from time import sleep
import RPi.GPIO as GPIO

url = "http://13.212.74.216:8081/machines/123abc"


def turnOnLED(pin):
    GPIO.output(pin,GPIO.HIGH)
    
def turnOffLED(pin):
    GPIO.output(pin,GPIO.LOW)
    
def moveAction():
    turnOffLED(red)
    turnOffLED(blue)
    turnOnLED(green)
    
def slowdownAction():
    turnOnLED(red)
    turnOffLED(blue)
    turnOnLED(green)

def stopAction():
    turnOnLED(red)
    turnOffLED(blue)
    turnOffLED(green)
    
def dispenseAction():
    turnOffLED(red)
    turnOnLED(blue)
    turnOffLED(green)

GPIO.setmode(GPIO.BCM)

red = 18
green = 17
blue = 27

GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue ,GPIO.OUT)


    
moveAction()
path = '/dev/'

files = []

for r, d, f in os.walk(path):
    for file in f:
        if 'ttyACM' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
    
ser = serial.Serial(
  
   port=f,
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0
bin_data = []
bin_flag = 0

try:
    
    print("test")
    
    while 1:
        
        
        response = requests.request("GET", url)
        t = response.json()
        machine_status = t[0][0]["status"]
        
        
        if machine_status == "stop":
            print("rest stop")
            stopAction()
            continue

        elif machine_status == "dispense":
            print("rest dispense")
            dispenseAction()

            continue
            
        elif machine_status == "move":
            print("rest move")
            moveAction()

        else:
            print("rest move1")
            moveAction()
        
        
        
        
        x = ""
        x = ser.readline()
        x = x.decode("utf-8")
        if (x != ""):
            if("bin_volume" in x):
                word_list = x.split(":")
                value = int(word_list[1])
                print(value)
                
                if value < 10:
                    print("stop")
                    stopAction()
                elif value >= 10 and value <=15:
                    print("slowdown")
                    slowdownAction()
                else:
                    print("move")
                    moveAction()
        
    
except KeyboardInterrupt:
    turnOffLED(red)
    turnOffLED(blue)
    turnOffLED(green)    
    
    pass