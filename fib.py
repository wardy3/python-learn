from itertools import tee


def firstn(it, n):
    return [next(it) for _ in range(n)]


def fib():
    # def _isum(g, h):
    #     while 1:
    #         yield next(g) + next(h)

    def _fib():
        yield 1
        yield 2
        next(fibTail)  # throw first away
        while True:
            yield next(fibHead) + next(fibTail)
        # for res in sum(next(fibHead), next(fibTail)):
        # for res in _isum(fibHead, fibTail):
        # yield res

    realfib = _fib()
    fibHead, fibTail, fibRes = tee(realfib, 3)
    return fibRes


print(firstn(fib(), 17))
