NATIVE_ATTRIBUTES = {'class_name', 'sid'}


class symm(object):

    def __init__(self, sid):
        # class_name = self.__class__.__name__.lower()
        print(f"We're underway with sid {sid}")
        # self.class_name = class_name
        self.sid = sid

    def __getattribute__(self, key):
        print(f'Some dickhead has asked me to get {key}')
        if key in NATIVE_ATTRIBUTES:
            return self.__dict__[key]
        else:
            return 'hello'
            # return Lazy(key)

    def __setattr__(self, key, value):
        print(f'Going to set key {key} to value {value}')
        if key in NATIVE_ATTRIBUTES:
            self.__dict__[key] = value
        else:
            self.key = value


class Lazy:
    def __init__(self, key):
        self.key = key

    @property
    def value(self):
        print(f'In lazy value with key {self.key}')
        print("Somehow need to look it up")

    def __repr__(self):
        print('represent...')
        return f'<Lazy {self.key}'

    def __str__(self):
        print('got to get a string...')
        return self.key


pri_array = symm('1381')

print(f'array code level is {pri_array.code}')

pri_array.code = 'new box'
print(f'array code level is {pri_array.code}')
