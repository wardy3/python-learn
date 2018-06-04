from random import *
from statistics import *
from collections import *

r = 1000000


def trial(): return r // 4 < median(sample(range(r), 5)) < 3 * r // 4


print(sum(trial() for i in range(r)) / r)


a = 5


def maths():
    u = 5*a + 5 + a**5
    v = 3*a + 3 + a**3
    w = 2*a + 2 + a**2
    x = 7*a + 7 + a**7


maths()
