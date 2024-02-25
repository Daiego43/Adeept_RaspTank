# My Rasptank
Hello there! I created this version of the rasptank code to be more modular
and start developing a ROS code. With this implementation you can instantiate 
the object **Rasptank**, (only one can be created).

To install:
```bash
pip install daiego43_rasptank
```

## Rasptan Control
To control the rasptank you can use the following methods:
```python
from daiego43_rasptank.rasptank import Rasptank
rasptank = Rasptank()
```

A rasptank object is composed of the following sensors and actuators:
```python
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
```

5 servos, 2 wheels, 1 camera, 1 ultrasonic sensor and 1 line sensor. The LEDs are not implemented.
Also all these classes are my own implementation and might have some errors.
But we can essentially get and set every sensor in the robot with some .