class desc(object):
    """Playing with data descriptors
    """

    # def __init__(self, name, attrkey=None):
        # print(f"init desc with name {name} and attrkey {attrkey}")
        # self.name = name
        # self.attrkey = attrkey

        # self.cache = dict()

    def __get__(self, obj, type=None):
        print(f"In desc __get__ with instance {obj} and type {type}")
        print(f"attrkey is {self.attrkey}")
        if obj is None:
            return self
        key = (obj if self.attrkey is None
               else getattr(obj, self.attrkey))
        print(f"trying key {key}")
        if key in self.cache:
            print(f"Got val {val}")
            return self.cache[key]
        else:
            print(f"can't find it. would generate")
            result = 98
            self.cache[key] = result
            return result


class crap:
    def __init__(self, name):
        print(f"init crap with name {name}")
        self.name = name
        self.num = 0

    @desc
    def inc(self):
        self.num += 1

    def add(self, add):
        self.num += add


x = crap('wardy')
print(x.num)
x.inc()
print(x.num)
x.add(5)
print(x.num)
