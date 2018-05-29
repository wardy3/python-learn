
import random


class wardy:
    def test(self):
        a = 3
        b = 4
        c = 5

        sum_squares = a*a + b*b + c*c
        x = sum_squares + 7
        y = sum_squares + 8
        z = sum_squares + 9

        print(x, y, z)

        t = (self.f_x(x))
        u = (self.f_x(y))
        v = (self.f_x(z))

        print("t %d u %d v %d" % (t, u, v, ))

    def f_x(self, x):
        return x*x + 2*x + 6


class Restaurant(object):
    bankrupt = False

    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")


def add1(x):
    print("Plain add")


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def addtwo(self, x):
        add1(x)
        add1(x)


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        self.face = random.randint(1, 6)

    def show(self):
        print("Die is showing", self.face)


class ColourDie(Die):
    def set_colour(self, colour):
        self.colour = colour

    def show(self):
        print("Die is showing", self.colour, self.face)


class Employee:
    def set_name(self, name):
        self.name = name


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        print("About to yield", index)
        yield data[index]


class scope:
    a = 'class a'
    b = 'class b'

    def __init__(self, a):
        print(self.a)
        self.a = a
        self._x = 123
        self.__y = 123
        b = 'meow'
        print(f'Never see {b:8s} again')
