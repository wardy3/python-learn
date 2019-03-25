from collections import OrderedDict
from itertools import tee
import pprint
from typing import Iterator

pp = pprint.PrettyPrinter(indent=4)


def intsfrom(i):
    while 1:
        yield i
        i += 1


def times(n: int, iterator: Iterator):
    for x in iterator:
        yield x * n


def merge(i1, i2):
    next_i1 = next(i1)
    next_i2 = next(i2)

    while True:
        if next_i1 < next_i2:
            yield next_i1
            next_i1 = next(i1)
        elif next_i2 < next_i1:
            yield next_i2
            next_i2 = next(i2)
        else:
            yield next_i1
            next_i1 = next(i1)
            next_i2 = next(i2)


# def generator(inc):
#     i = 1
#     yield i
#     while True:
#         i += inc
#         yield i


def firstn(it, n):
    return [next(it) for _ in range(n)]
    # for _ in range(n):
    #     yield next(it)


def m235():
    def _m235():
        yield 1
        # for n in merge(times(2, m2), times(3, m3)):
        for n in merge(times(2, m2), merge(times(3, m3), times(5, m5))):
            yield n

    m1 = _m235()
    m2, m3, m5, mRes = tee(m1, 4)
    return mRes


def main():

    # x = firstn(intsfrom(5), 7)
    # print(f"x {x}")
    # assert x == [5, 6, 7, 8, 9, 10, 11]

    # x = [i for i in merge(iter([1, 3, 5]), iter([2, 4, 5, 6]))]
    # print(f"x {x}")
    # assert x == [1, 2, 3, 4, 5, 6]

    it = m235()
    for i in range(5):
        print(firstn(it, 15))

    report = dict()
    for i in range(5):
        for j in range(5):
            for k in range(5):
                total = pow(2, i) * pow(3, j) * pow(5, k)
                report[(i, j, k)] = total
                print(f"2^{i} 3^{j} 5^{k} = {total}")
    report_sort = OrderedDict(sorted(report.items(), key=lambda x: x[1]))
    # report_sort = sorted(report.{k: report[k] for k in sorted(report, key=report.get)}
    # report_sort = {k: report[k] for k in sorted(report, key=report.get)}
    print(f"report {pp.pformat(report_sort)}")

    #     l1 = [x for x in range(10)]
    #     l2 = [x*1.5 for x in range(10)]
    #     i1 = iter(l1)
    #     i2 = iter(l2)

    # print(f"l1 {l1}")
    # print(f"l2 {l2}")

    # i1 = generator(1)
    # i2 = generator(1.5)
    # i3 = times(i2, 2.5)

    # for i in merge(i1, i3):
    #     print(f"i is {i}")


if __name__ == "__main__":
    main()
"""

>>> from itertools import tee
>>> def m235():
...     def _m235():
...         yield 1
...         for n in merge(times(2, m2),
...                        merge(times(3, m3),
...                              times(5, m5))):
...             yield n
...     m1 = _m235()
...     m2, m3, m5, mRes = tee(m1, 4)
...     return mRes

>>> it = m235()
>>> for i in range(5):
...     print(firstn(it, 15))

"""
