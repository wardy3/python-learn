import random


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")
        print(type(self))
        print(dir(self))
        # print(f"collar is {self.collar}")


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print(f"{self.name} is fetching {thing}")
        self.collar = 'dirty'


class Cat(Animal):
    def swatstring(self):
        print(f"{self.name} shreds the string")


class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


def main():
    r = Dog('Rover')
    r.fetch('stick')
    r.eat('poo')

    f = Cat('Tom')
    f.swatstring()
    f.eat('tuna')

    D.mro()  # Show method inheritance order


if __name__ == '__main__':
    main()
