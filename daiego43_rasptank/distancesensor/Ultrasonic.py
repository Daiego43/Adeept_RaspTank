# For some reason,
# gpiozero library does not work with ultrasonic sensor
# so we will use RPi.GPIO library

import time
import RPi.GPIO as GPIO

class DistanceSensor:
    def __init__(self, triger_pin=11, echo_pin=8):
        self.triger_pin = triger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(triger_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(echo_pin, GPIO.IN)
    def get_data(self):       # A function that measures the distance
        """
        Data returned is distance in cm
        """
        GPIO.output(self.triger_pin, GPIO.HIGH)  # Set the trigger end to high level for 10us
        time.sleep(0.00001)
        GPIO.output(self.triger_pin, GPIO.LOW)
        while not GPIO.input(self.echo_pin):  # Wait for the echo end to return high level
            pass
        t1 = time.time()
        while GPIO.input(self.echo_pin):  # Wait for the echo end to return high level
            pass
        t2 = time.time()
        return (t2-t1)*340/2*100  # The distance is calculated based on the time difference between the two signals

if __name__ == '__main__':
    distance_sensor = DistanceSensor()
    try:
        while True:
            print("Distance: %.2f cm" % distance_sensor.get_data())  # Print the distance
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up the GPIO resources