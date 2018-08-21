class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")
        print(type(self))
        print(dir(self))
        # print(f"collar is {self.collar}")


class Dog(Animal):
    def fetch(self, thing):
        print(f"{self.name} is fetching {thing}")
        self.collar = 'dirty'


class Cat(Animal):
    def swatstring(self):
        print(f"{self.name} shreds the string")


r = Dog('Rover')
r.fetch('stick')
r.eat('poo')

f = Cat('Tom')
f.swatstring()
f.eat('tuna')
