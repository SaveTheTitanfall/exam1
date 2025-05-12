import json
from datetime import datetime
import random

class TemperatureSensor:
    def __init__(self, name="Sensor T"):
        self.name = name

    def read(self):
        # litle bit of random noise
        return round(random.uniform(15.0, 25.0), 2)

class TemperatureRecord:
    def __init__(self, temperature):
        self.temperature = temperature
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "temperature": self.temperature,
            "timestamp": self.timestamp
        }

class Logger:
    def __init__(self, num_entries, filename="temp_log.json"):
        self.num_entries = num_entries
        self.filename = filename
        self.data = []

    def collect_data(self, sensor):
        for _ in range(self.num_entries):
            temp = sensor.read()
            record = TemperatureRecord(temp)
            self.data.append(record.to_dict())

    def save(self):
        with open(self.filename, "w" ) as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
        print(f"saved in: {self.filename}")
if __name__ == "__main__":
    sensor = TemperatureSensor()
    logger = Logger(num_entries=3)
    logger.collect_data(sensor)
    logger.save()