import time
from gpiozero import OutputDevice, DigitalInputDevice


class UltrasonicSensor:
    def __init__(self, trigger_pin=17, echo_pin=14):
        self.trigger = OutputDevice(trigger_pin)
        self.echo = DigitalInputDevice(echo_pin)

    def get_distance(self):
        self.trigger.on()
        time.sleep(0.00001)
        self.trigger.off()
        start_time = time.time()
        while not self.echo.is_active:
            start_time = time.time()
        while self.echo.is_active:
            stop_time = time.time()
        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2
        return round(distance, 2)


if __name__ == '__main__':
    # Asegúrate de ajustar los pines según tu conexión
    sensor = UltrasonicSensor(trigger_pin=17, echo_pin=14)
    try:
        while True:
            distance = sensor.get_distance()
            print(f"Distance: {distance} cm")
            time.sleep(1)
    except KeyboardInterrupt:
        pass
