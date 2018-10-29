from math import fsum, sqrt
from typing import Iterable, Tuple


Point = Tuple[float, ...]


def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip)->float:
    """Euclidean distance function for multi-dimensional data
    """

    # print(f"dist p {list(p)} q{list(q)}")

    return sqrt(fsum([(value1-value2)**2 for value1, value2 in zip(p, q)]))


p1 = (1, 2, 3)
p2 = (4, 5, 6)

dist1_2 = dist(p1, p2)

print(f"1st distance is {dist1_2}")


p3 = (1.5, 2, 3)
p4 = (4, 9.5, 6)

dist3_4 = dist(p3, p4)

print(f"2nd distance is {dist3_4}")
