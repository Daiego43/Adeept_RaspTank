"""

"""
import time
import RPi.GPIO as GPIO


class Motor:
    def __init__(self, wheel, pin1, pin2, en):
        self.wheel = wheel
        self.pin1 = pin1
        self.pin2 = pin2
        self.en = en
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)
        self.stop()
        self.pwm = GPIO.PWM(self.en, 1000)
        print("Motor Motor: " + self.wheel)
        time.sleep(1)

    def stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.en, GPIO.LOW)

    def backward(self, speed, radius=1):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(speed * radius)

    def forward(self, speed, radius=1):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)
        self.pwm.start(100)
        self.pwm.ChangeDutyCycle(speed * radius)


class LeftWheel(Motor):
    def __init__(self):
        super().__init__("left", 27, 18, 17)

    def forward(self, speed, radius=1):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
        self.pwm.start(100)
        self.pwm.ChangeDutyCycle(speed * radius)

    def backward(self, speed, radius=1):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(speed * radius)


class RightWheel(Motor):
    def __init__(self):
        super().__init__("right", 14, 15, 4)
