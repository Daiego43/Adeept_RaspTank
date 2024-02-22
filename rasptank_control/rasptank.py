from servo.Servo import Servo
from motor.Motor import LeftWheel, RightWheel
from distancesensor.Ultrasonic import DistanceSensor
from camera.Camera import Camera
from linesensor.LineSensor import MyLineSensor
import time

class Rasptank:
    def __init__(self):
        # Brazo del robot
        self.link_4 = Servo(15, "end_effector", min_angle=0, max_angle=90, home_angle=90)
        self.link_3 = Servo(14, "wrist", min_angle=0, max_angle=180, home_angle=80)
        self.link_2 = Servo(13, "elbow", min_angle=0, max_angle=135, home_angle=110)
        self.link_1 = Servo(12, "base", min_angle=0, max_angle=180, home_angle=120)
        self.link_0 = Servo(11, "camera", min_angle=70, max_angle=120, home_angle=110)

        # Camara del robot
        self.video = Camera()

        # Ruedas del robot
        self.left_wheel = LeftWheel()
        self.right_wheel = RightWheel()

        # Sensor distancesensor
        self.ultrasonic_sensor = DistanceSensor()

        # Sensor de linea
        self.line_follower = MyLineSensor()


    def move_forward(self, left_speed=1, right_speed=1):
        self.left_wheel.forward(left_speed)
        self.right_wheel.forward(right_speed)

    def move_backward(self, left_speed=1, right_speed=1):
        self.left_wheel.backward(left_speed)
        self.right_wheel.backward(right_speed)

    def turn_left(self, left_speed=1, right_speed=1):
        self.left_wheel.backward(left_speed)
        self.right_wheel.forward(right_speed)

    def turn_right(self, left_speed=1, right_speed=1):
        self.left_wheel.forward(left_speed)
        self.right_wheel.backward(right_speed)

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()


if __name__ == '__main__':
    rasptank = Rasptank()
    rasptank.link_0.motion_goal(0)
    rasptank.move_forward()
    time.sleep(5)
    rasptank.stop()
    print(rasptank.ultrasonic_sensor.get_dist())
    print(rasptank.line_follower.get_status())
    rasptank.video.save_frame("test.jpg")

