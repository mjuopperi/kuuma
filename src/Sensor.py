import re


class Sensor:
    def __init__(self, sensor_path, config):
        sensor_id = self.parse_sensor_id(sensor_path)
        self.id = sensor_id
        self.path = sensor_path
        self.name = self.id_to_name(sensor_id, config)

    def get_temperature(self):
        with open(self.path, 'r') as file:
            temperature = self.parse_temperature(file.readlines()[-1])
            return round(temperature / 1000, 2)

    @staticmethod
    def id_to_name(sensor_id, config):
        return config.get(sensor_id, 'Unknown')

    @staticmethod
    def parse_temperature(data):
        regex = re.search('t=(-?\d+)', data)
        if regex:
            return float(regex.group(1))
        else:
            return None

    @staticmethod
    def parse_sensor_id(path):
        regex = re.search('/([\w-]+)/w1_slave', path)
        if regex:
            return regex.group(1)
        else:
            return None
