import sys
from collections import defaultdict


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
        if n % i:
            pass
        else:
            factors.add(i)
    return factors


def aliquot(n):
    return sum(proper_divisors(n))


def untouchable(n):
    pass


if (len(sys.argv) == 1):
    start, stop = 1, 20
elif (len(sys.argv) == 2):
    start, stop = 1, sys.argv[1]
else:
    start, stop = sys.argv[1: 3]

stats = defaultdict(int)

start = int(start)
stop = int(stop)

for n in range(start, stop+1):
    # factors = proper_divisors(n)
    ali_sum = aliquot(n)
    if ali_sum == 1:
        num_class = 'prime'
    elif ali_sum == n:
        num_class = 'perfect'
    elif ali_sum > n:
        num_class = 'abundant'
    elif ali_sum < n:
        num_class = 'deficient'
    else:
        raise ValueError

    stats[num_class] += 1
    stats['total'] += 1

    print(
        f"n {n:8d}\tali {ali_sum:8d}\t{num_class:9s}"
        f"\t{stats[num_class]*100/stats['total']:5.1f}%")
