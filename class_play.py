class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


class Dog2:

    kind = 'canine'

    def __init__(self, name):

        self.name = name

    def set_kind(self, kind):
        self.kind = kind

    def __get__(self, getarg):
        print(f"in __get__ {getarg}")
