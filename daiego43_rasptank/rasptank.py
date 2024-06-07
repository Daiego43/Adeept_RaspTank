from daiego43_rasptank.servo.Servo import Servo
from daiego43_rasptank.motor.Motor import LeftWheel, RightWheel
from daiego43_rasptank.distancesensor.Ultrasonic import DistanceSensor
from daiego43_rasptank.camera.Camera import Camera
from daiego43_rasptank.linesensor.LineSensor import MyLineSensor


class Singleton:
    _instance = None  # Atributo de clase para almacenar la única instancia

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance


class Rasptank(Singleton):
    def __init__(self):
        if self._initialized: return
        self._initialized = True
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

    def get_line_follower_data(self):
        return self.line_follower.get_data()

    def get_ultrasonic_sensor_data(self):
        return self.ultrasonic_sensor.get_data()

    def get_camera_frame(self):
        return self.video.get_frame()


if __name__ == '__main__':
    rasptank = Rasptank()
    rasptank.video.save_frame("test.jpg")
