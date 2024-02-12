class Vehicle:
    def __init__(self):
        self.type = "generic vehicle"

class Car(Vehicle):
    def __init__(self, color, sound):
        super(Car, self).__init__()
        self.type = "car"
        self.color = color
        self.sound = sound
        self.wheels = 4

class Motorcycle(Vehicle):
    def __init__(self, color, sound):
        super(Motorcycle, self).__init__()
        self.type = "motorcycle"
        self.color = color
        self.sound = sound
        self.wheels = 0

class Boat(Vehicle):
    def __init__(self, color, sound):
        super(Boat, self).__init__()
        self.type = "boat"
        self.color = color
        self.sound = sound
        self.wheels = 0