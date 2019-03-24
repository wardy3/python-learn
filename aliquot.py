from collections import defaultdict
import sys
from typing import Union


def prime_factors(n):
    start_n = n
    i = 2
    factors = set()
    if n != 1:
        factors.add(1)
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1 and n != start_n:
        factors.add(n)
    return factors


def proper_divisors(n):
    factors = set()
    for i in range(1, n):
        if not n % i:
            factors.add(i)
    return factors


def aliquot(n):
    return sum(proper_divisors(n))


def untouchable(n):
    pass


start: Union[int, str]
stop: Union[int, str]
if (len(sys.argv) == 1):
    start, stop = 1, 20
elif (len(sys.argv) == 2):
    start, stop = 1, sys.argv[1]
else:
    start, stop = sys.argv[1:3]

stats: dict = defaultdict(int)

start = int(start)
stop = int(stop)

for n in range(start, stop + 1):
    # factors = proper_divisors(n)
    ali_sum = aliquot(n)
    if ali_sum == 1:
        number_class = 'prime'
    elif ali_sum == n:
        number_class = 'perfect'
    elif ali_sum > n:
        number_class = 'abundant'
    elif ali_sum < n:
        number_class = 'deficient'
    else:
        raise ValueError

    stats[number_class] += 1
    stats['total'] += 1

    print(f"n {n:8d}\tali {ali_sum:8d}\t{number_class:9s}")
    #   f"\t{stats[number_class]*100/stats['total']:5.1f}%")

total = stats.pop('total')

for number_class in stats:
    print(f"{number_class:10s}{stats[number_class]*100/total:5.1f}%")
# print(stats)
