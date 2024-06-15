from gpiozero import OutputDevice, PWMOutputDevice
import time


class Motor:
    def __init__(self, wheel, pin1, pin2, en):
        self.wheel = wheel
        self.forward_pin = OutputDevice(pin1, initial_value=False)
        self.backward_pin = OutputDevice(pin2, initial_value=False)
        self.enable_pin = PWMOutputDevice(en, frequency=1000)
        print("Motor initialized: " + self.wheel)
        time.sleep(1)

    def stop(self):
        self.forward_pin.off()
        self.backward_pin.off()
        self.enable_pin.off()

    def move(self, speed=0):
        if speed < 0:
            self.backward(speed)
        elif speed > 0:
            self.forward(speed)
        else:
            self.stop()

    def backward(self, speed=1):
        self.enable_pin.value = speed
        match self.wheel:
            case "left":
                self.backward_pin.on()
                self.forward_pin.off()
            case "right":
                self.forward_pin.on()
                self.backward_pin.off()

    def forward(self, speed=1):
        self.enable_pin.value = speed
        match self.wheel:
            case "left":
                self.forward_pin.on()
                self.backward_pin.off()
            case "right":
                self.backward_pin.on()
                self.forward_pin.off()


class LeftWheel(Motor):
    def __init__(self):
        super().__init__("left", 27, 18, 17)


class RightWheel(Motor):
    def __init__(self):
        super().__init__("right", 14, 15, 4)


if __name__ == '__main__':
    right, left = RightWheel(), LeftWheel()
    right.forward()
    left.forward()
    time.sleep(2)
    right.stop()
    left.stop()
    time.sleep(2)
    right.backward()
    left.backward()
    time.sleep(2)
    right.stop()
    left.stop()
