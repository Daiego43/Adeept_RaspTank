import Adafruit_PCA9685  # Import the library used to communicate with PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()  # Instantiate the object used to control the PWM
pwm.set_pwm_freq(50)  # Set the frequency of the PWM signal


class Servo:
    def __init__(self, pin, name="default", min_angle=0, max_angle=180, home_angle=0, motion_step=1):
        self.pin = pin
        self.name = name
        self.home = home_angle
        self.current_angle = home_angle
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.motion_step = motion_step
        self.set_angle(self.current_angle)
        print("Iniciado servo: " + self.name)
        time.sleep(1)

    def set_angle(self, angle):
        angle = self.clamp_value(angle)
        power = round(angle * 2.55 + 100)
        pwm.set_pwm(self.pin, 0, power)
        self.current_angle = angle

    def get_angle(self):
        return self.current_angle

    def clamp_value(self, angle):
        if angle < self.min_angle:
            angle = self.min_angle
        if angle > self.max_angle:
            angle = self.max_angle
        return angle

    def increase_angle(self):
        self.set_angle(self.current_angle + self.motion_step)

    def decrease_angle(self):
        self.set_angle(self.current_angle - self.motion_step)

    def motion_goal(self, angle_goal):
        if angle_goal > self.current_angle:
            for i in range(self.current_angle, angle_goal, self.motion_step):
                self.set_angle(i)
                time.sleep(0.03)
        else:
            for i in range(self.current_angle, angle_goal, -self.motion_step):
                self.set_angle(i)
                time.sleep(0.03)

        if angle_goal != self.current_angle:
            self.set_angle(angle_goal)


def test_servos():
    pinza = Servo(15, "pinza", min_angle=0, max_angle=90, home_angle=90)
    muneca = Servo(14, "muneca", min_angle=0, max_angle=180, home_angle=75)
    codo = Servo(13, "codo", min_angle=0, max_angle=135, home_angle=70)
    brazo = Servo(12, "brazo", min_angle=0, max_angle=180, home_angle=80)
    camara = Servo(11, "camara", min_angle=70, max_angle=120, home_angle=110)
    print("Espera...", end="")
    for i in range(1, 4):
        print(i, "...", end="")
        time.sleep(1)
    print()

    for servo in [pinza, muneca, codo, brazo, camara]:
        print("Servo: " + servo.name)
        if servo.name == "codo":
            brazo.motion_goal(brazo.max_angle)
        servo.motion_goal(servo.max_angle)
        time.sleep(5)
        servo.motion_goal(servo.min_angle)
        time.sleep(5)
        servo.motion_goal(servo.home)
        time.sleep(5)
        if servo.name == "codo":
            servo.motion_goal(servo.min_angle)


def init_pos_servos():
    brazo = Servo(12, "brazo", min_angle=0, max_angle=180, home_angle=120)
    codo = Servo(13, "codo", min_angle=0, max_angle=135, home_angle=110)
    pinza = Servo(15, "pinza", min_angle=0, max_angle=90, home_angle=90)
    muneca = Servo(14, "muneca", min_angle=0, max_angle=180, home_angle=75)
    camara = Servo(11, "camara", min_angle=70, max_angle=120, home_angle=110)
    return brazo, codo, pinza, muneca, camara


if __name__ == '__main__':
    init_pos_servos()
