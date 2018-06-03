# Make a descriptor which does lazy lookups when needed
class LazyProperty(object):
    def __init__(self, defer):
        self.cache = dict()
        self.defer = defer

    def __get__(self, instance, type=None):
        print(f"instance {instance} type {type}")
        if instance is None:
            return self
        key = (instance if self.attrkey is None
               else getattr(instance, self.attrkey))
        if key in self.cache:
            return self.cache[key]
        else:
            result = self.deferred_computation(instance)
            self.cache[key] = result
            return result

    @staticmethod
    def decorate(**kwargs):
        def decorator(func):
            return LazyProperty(func, **kwargs)
        return decorator


class Factorization(object):
    def __init__(self, n):
        self.n = n

    @LazyProperty
    def factors(self):
        print("computing factors of %d" % self.n)
        t1 = time.time()
        result = primefac.factorint(self.n)
        t2 = time.time()
        print("elapsed time: %.3f s" % (t2 - t1))
        return result

    def __repr__(self):
        return "Factorization(%d)" % self.n
