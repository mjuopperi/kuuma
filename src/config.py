import configparser


def parse_config():
    config = configparser.ConfigParser()
    config.read_file(open(r'config.properties'))

    return {
        'influxdb': {
            'host': config.get('influxdb', 'host'),
            'port': config.get('influxdb', 'port'),
            'user': config.get('influxdb', 'user'),
            'password': config.get('influxdb', 'password'),
            'database': config.get('influxdb', 'database'),
        },
        'sensors': dict(config.items('sensors')),
    }
