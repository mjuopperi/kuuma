from RPi import GPIO
import glob
import time
from src.DB import DB
from src.Sensor import Sensor
from src.config import parse_config


class Main:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.config = parse_config()
        self.db = DB(self.config['influxdb'])
        self.sensors = []

    def start(self):
        self.sensors = self.find_temperature_sensors(self.config['sensors'])
        print('Found {} sensors'.format(len(self.sensors)))
        while True:
            start = time.time()
            self._measure_temperatures()
            duration = (time.time() - start)
            time.sleep(max(10 - duration, 0))

    def _measure_temperatures(self):
        for sensor in self.sensors:
            temperature = sensor.get_temperature()
            print('Saving {:.2f} C for {}'.format(temperature, sensor.name))
            self.db.insert_temperature(sensor, temperature)

    @staticmethod
    def find_temperature_sensors(config):
        return list(map(lambda path: Sensor(path, config), glob.glob('/sys/bus/w1/devices/28*/w1_slave')))


try:
    poller = Main()
    poller.start()
except KeyboardInterrupt:
    print('Stopping...')
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
