import time
import RPi.GPIO as GPIO

line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20


class LineFollower:
    def __init__(self):
        self.line_pin_right = 19
        self.line_pin_middle = 16
        self.line_pin_left = 20
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(line_pin_right, GPIO.IN)
        GPIO.setup(line_pin_middle, GPIO.IN)
        GPIO.setup(line_pin_left, GPIO.IN)

    # motor.setup()
    def get_status(self):
        status_right = GPIO.input(line_pin_right)
        status_middle = GPIO.input(line_pin_middle)
        status_left = GPIO.input(line_pin_left)
        return status_right, status_middle, status_left


if __name__ == "__main__":
    line_follower = LineFollower()
    while True:
        status_right, status_middle, status_left = line_follower.get_status()
        print(f"Right: {status_right}, Middle: {status_middle}, Left: {status_left}")
        time.sleep(0.1)
