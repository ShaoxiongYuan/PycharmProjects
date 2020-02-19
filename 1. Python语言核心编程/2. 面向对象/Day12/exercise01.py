class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        print("跑")


class Bird(Animal):
    def fly(self):
        print("飞")


a1 = Animal()
d1 = Dog()
b1 = Bird()

d1.eat()
a1.eat()
d1.run()
b1.fly()

print(isinstance(a1, Animal))
print(isinstance(d1, Animal))
print(isinstance(d1, Bird))
print(isinstance(b1, Bird))

print(issubclass(Animal, Dog))
print(issubclass(Dog, Animal))
print(issubclass(Bird, Animal))
print(issubclass(Bird, Dog))

print(type(a1) == Animal)
print(type(d1) == Animal)
print(type(d1) == Bird)
print(type(b1) == Bird)
