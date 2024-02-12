import time
from gpiozero import DistanceSensor



class UltrasonicSensor:
    def __init__(self, trigger_pin=11, echo_pin=8):
        self.distance_sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin)

    def get_distance(self):
        return self.distance_sensor.distance * 100



if __name__ == '__main__':
    # Asegúrate de ajustar los pines según tu conexión
    sensor = UltrasonicSensor()
    try:
        while True:
            distance = sensor.get_distance()
            print(f"Distance: {distance} cm")
            time.sleep(1)
    except KeyboardInterrupt:
        pass
