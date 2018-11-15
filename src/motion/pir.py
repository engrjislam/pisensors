import RPi.GPIO as GPIO
import time


pirPin = 7 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pirPin, GPIO.IN)

try: 
    while True:
        if GPIO.input(pirPin) == 0:
            print("No Motion!")
        else:
            print("Motion detected!")
        time.sleep(1)
except KeyboardInterrupt:
    print('Exited ... ')

GPIO.cleanup()
    
