import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
trigger_pin = 27
echo_pin = 17
 
#set GPIO direction (IN / OUT)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(trigger_pin, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)
 
    # Wait for rising edge
    while GPIO.input(echo_pin) == 0:
        pass
        # Do nothing
    startTime = time.time()
 
    # Wait for falling edge
    while GPIO.input(echo_pin) == 1:
        pass
    
    # Calculate basic distance 
    distance = ((time.time() - startTime) * 34300) / 2
 
    return startTime, distance
 
# Actual running code

try:
    while True:
        timestamp, dist = distance()
        print (f"Timestamp: {timestamp}, Distance = {dist} cm")
        time.sleep(0.1)

    # Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Manual stop")
    GPIO.cleanup()