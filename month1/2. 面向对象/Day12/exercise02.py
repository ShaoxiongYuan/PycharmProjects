class Car:
    def __init__(self, brand="", price=0):
        self.brand = brand
        self.price = price


class Motor(Car):
    def __init__(self, brand="", price=0, volume=0, power=0):
        super().__init__(brand, price)
        self.volume = volume
        self.power = power


c1 = Car()
m1 = Motor("丰田")
print(m1.brand)
