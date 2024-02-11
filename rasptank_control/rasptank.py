from servos import ServoControl
from motores import MotorControl
from ultrasonido import Ultrasonic
from camara import Camera
from siguelinea import LineFollower
import time

class Rasptank:
    def __init__(self):
        # Brazo del robot
        self.pinza = ServoControl.Servo(15, "pinza", min_angle=0, max_angle=90, home_angle=90)
        self.muneca = ServoControl.Servo(14, "muneca", min_angle=0, max_angle=180, home_angle=80)
        self.codo = ServoControl.Servo(13, "codo", min_angle=0, max_angle=135, home_angle=110)
        self.brazo = ServoControl.Servo(12, "brazo", min_angle=0, max_angle=180, home_angle=120)

        # Camara del robot
        self.servo_camara = ServoControl.Servo(11, "camara", min_angle=70, max_angle=120, home_angle=110)
        self.camara = Camera.Camera()

        # Ruedas del robot
        self.left_wheel = MotorControl.LeftWheel()
        self.right_wheel = MotorControl.RightWheel()

        # Sensor ultrasonido
        self.ultrasonic_sensor = Ultrasonic.UltrasonicSensor()

        # Sensor de linea
        self.line_follower = LineFollower.LineFollower()


    def move_forward(self, speed=100, radius=1):
        self.left_wheel.forward(speed, radius)
        self.right_wheel.forward(speed, radius)

    def move_backward(self, speed=100, radius=1):
        self.left_wheel.backward(speed, radius)
        self.right_wheel.backward(speed, radius)

    def turn_left(self, speed=100, radius=1):
        self.left_wheel.backward(speed, radius)
        self.right_wheel.forward(speed, radius)

    def turn_right(self, speed=100, radius=1):
        self.left_wheel.forward(speed, radius)
        self.right_wheel.backward(speed, radius)

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()


if __name__ == '__main__':
    rasptank = Rasptank()
    rasptank.move_forward()
    time.sleep(5)
