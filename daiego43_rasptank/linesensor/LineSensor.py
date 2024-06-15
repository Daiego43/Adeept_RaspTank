import time
from gpiozero import LineSensor

# Define los pines para el sensor de línea
line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

class MyLineSensor:
    def __init__(self, right_pin=19, middle_pin=16, left_pin=20):
        # Inicializa los sensores de línea
        self.sensor_right = LineSensor(right_pin)
        self.sensor_middle = LineSensor(middle_pin)
        self.sensor_left = LineSensor(left_pin)

    def get_data(self):
        # Obtiene el estado de cada sensor
        # True indica línea detectada; False indica línea no detectada
        status_right = self.sensor_right.value
        status_middle = self.sensor_middle.value
        status_left = self.sensor_left.value
        return status_left, status_middle, status_right

if __name__ == "__main__":
    line_follower = MyLineSensor()
    while True:
        status_left, status_middle, status_right = line_follower.get_data()
        print(f"Right: {status_right}, Middle: {status_middle}, Left: {status_left}")
        time.sleep(0.1)
