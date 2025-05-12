class Sensor:
    def __init__(self, name, sensor_type, unit):
        self.name = name
        self.sensor_type = sensor_type
        self.unit = unit

    def get_name(self):
        return self.name

    def get_type(self):
        return self.sensor_type

    def get_unit(self):
        return self.unit

    def __str__(self):
        return f"Сенсор {self.sensor_type}: {self.name} ({self.unit})"


class ComponentManager:
    def __init__(self):
        self.inventory = []

    def add_sensor(self, sensor):
        self.inventory.append(sensor)

    def get_all_sensors(self):
        return self.inventory

    def find_sensor_by_name(self, name):
        return next((s for s in self.inventory if s.get_name() == name), None)

    def remove_sensor(self, name):
        self.inventory = [s for s in self.inventory if s.get_name() != name]

    def count_sensors(self):
        return len(self.inventory)


class SensorInventory(Sensor, ComponentManager):
    def __init__(self):
        ComponentManager.__init__(self)

    def __str__(self):
        if not self.inventory:
            return "there no staff."
        return "\n".join(str(sensor) for sensor in self.inventory)
sens=Sensor("Sensor1", "Temperature", "Celsius")
print(sens.get_name())