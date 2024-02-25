"""
Modulo para controlar e instanciar los Servos utilizando
la libreria Adafruit_PCA9685 (Descargar esta librería por si desaparece de internet)
"""

import time
import Adafruit_PCA9685  # Import the library used to communicate with PCA9685


class Servo:
    pwm = Adafruit_PCA9685.PCA9685()  # Instantiate the object used to control the PWM
    pwm.set_pwm_freq(50)

    def __init__(self, pin, name="default", min_angle=0, max_angle=180, home_angle=0,
                 motion_step=1):
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
        self.pwm.set_pwm(self.pin, 0, power)
        self.current_angle = angle

    def get_angle(self):
        return self.current_angle

    def clamp_value(self, angle):
        if angle <= self.min_angle:
            angle = self.min_angle
        if angle >= self.max_angle:
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


def init_pos_servos():
    pinza = Servo(15, "pinza", min_angle=0, max_angle=90, home_angle=90)
    muneca = Servo(14, "muneca", min_angle=0, max_angle=180, home_angle=80)
    codo = Servo(13, "codo", min_angle=0, max_angle=135, home_angle=110)
    brazo = Servo(12, "brazo", min_angle=0, max_angle=180, home_angle=120)
    camara = Servo(11, "camera", min_angle=70, max_angle=120, home_angle=110)

    return pinza, muneca, codo, brazo, camara


if __name__ == '__main__':
    pinza, muneca, codo, brazo, camara = init_pos_servos()
