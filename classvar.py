class YourClass(object):
    classy = 10

    def set_val(self):
        self.insty = 100

    def calc_sum(sum=sum, vsum=vsum, average=average):
        d = sum(a, b)


dd = YourClass()
ee = YourClass()

print(dd.classy)
print(ee.classy)

YourClass.classy = 'hi dice'

print(dd.classy)
print(ee.classy)

dd.classy = 'too noisy'
print(dd.classy)
del dd.classy
print(dd.classy)
del dd.classy
print(dd.classy)

'''
dd.set_val()

print(dd.classy)
print(dd.insty)

ee = YourClass()
ee.classy = 200

print(dd.classy)
print(ee.classy)
'''
