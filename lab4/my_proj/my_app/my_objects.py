class Vehicle:
    def __init__(self):
        self.type = "generic vehicle"

class Car(Vehicle):
    def __init__(self, color, sound):
        self.type = "car"
        self.color = color
        self.sound = sound
        self.wheels = 4

class Boat(Vehicle):
    def __init__(self, color, sound):
        super(Boat, self).__init__()
        self.color = color
        self.sound = sound
        self.wheels = 0