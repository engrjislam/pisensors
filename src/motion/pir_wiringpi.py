import wiringpi
import time


SENSOR_PIN = 7
INPUT, OUTPUT = 0, 1
LOW, HIGH = 0, 1

 
# One of the following MUST be called before using IO functions:
wiringpi.wiringPiSetup()      # For sequential pin numbering
'''
# OR
wiringpi.wiringPiSetupSys()   # For /sys/class/gpio with GPIO pin numbering
# OR
wiringpi.wiringPiSetupGpio()  # For GPIO pin numbering
'''

wiringpi.pinMode(SENSOR_PIN, INPUT) 	# Set pin 7 to 0 ( INPUT )
#wiringpi.digitalWrite(SENSOR_PIN, LOW)  	# Write 1 ( HIGH ) to pin 7
#wiringpi.digitalRead(SENSOR_PIN)      	# Read pin 7
 
try:
    while True:
        if wiringpi.digitalRead(SENSOR_PIN) == HIGH:
            print('Motion detected!')
        else:
            print('No Motion!')
        time.sleep(1)
except KeyboardInterrupt:
    print("Finish...")

#wiringpi.digitalWrite(SENSOR_PIN, LOW)