import time
import RPi.GPIO as GPIO


class UltrasonicSensor:
    def __init__(self):
        self.TRIG = 11
        self.ECHO = 8
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ECHO, GPIO.IN)

    def get_distance(self):
        GPIO.output(self.TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, GPIO.LOW)
        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance


if __name__ == '__main__':
    sensor = UltrasonicSensor()
    try:
        while True:
            print(sensor.get_distance())
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
