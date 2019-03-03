from influxdb import InfluxDBClient


class DB:
    def __init__(self, config):
        self.client = InfluxDBClient(
            config['host'],
            config['port'],
            config['user'],
            config['password'],
            config['database']
        )
        self.client.create_database(config['database'])

    def insert_temperature(self, sensor, temperature):
        json_body = [
            {
                "measurement": "temperature",
                "tags": {
                    "sensor_id": sensor.id,
                    "sensor_name": sensor.name,
                },
                "fields": {
                    "value": temperature
                }
            }
        ]
        self.client.write_points(json_body)
