class Decorator(object):

    def __init__(self, f):
        print(f"init this with {f}")
        self.f = f

    def __call__(self, *args, **kwargs):
        print(f"call this with args <{args}> kwargs <{kwargs}>")
        self.f(self2, *args, **kwargs)


class test(object):

    @Decorator
    def crap(self, string):
        print(f"In crap string {string}")
        self.f = 9


# test.crap('a', 'b')
x = test()

x.crap('boo')
x.crap('pop')


class symm(object):
    def __init__(self, sid):
        self.sid = sid

    def devinfo(self, dev):
        return self.cache['devinfo'].gb


symm1 = symm('1381')
