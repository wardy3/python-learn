class MyClass:
    var = 1

    def method(self):
        print(f"in method with self {self}")


this_obj = MyClass()
that_obj = MyClass()

this_obj.method()
that_obj.method()

MyClass.method(this_obj)
