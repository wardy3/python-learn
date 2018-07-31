from pprint import pprint


class wardy():
    def __init__(self):
        print(f"wardy init'd")

    def __setattr__(self, var, value):
        print(f"super set")
        super().__setattr__("a"+var, value+1)


class record(wardy):
    def __setattr__(self, var, value):
        print(f"trying to set var {var}")
        if var not in ("x", "y", "z"):
            raise ValueError
        else:
            print(f"var {var} value {value} super {super()} class {__class__}")
            super().__setattr__(var, value)

    def hi_dice(self):
        print(f"hi dice")


print(f"start")

a = record()

a.x = 1
a.y = 2
a.z = 3

pprint(a.__dict__)

b = record()

b.x = 4
b.y = 5
b.z = 6


print(f"{a.ax} {a.ay}")
print(f"{b.ax} {b.ay}")
