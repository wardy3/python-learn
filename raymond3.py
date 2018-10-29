# zip

from pprint import pprint

list(zip('abcdef', 'ghijklm'))
# [('a', 'g'), ('b', 'h'), ('c', 'i'), ('d', 'j'), ('e', 'k'), ('f', 'l')]

from itertools import zip_longest
# print(list(zip_longest('abcdef', 'ghijklm')))
# [('a', 'g'), ('b', 'h'), ('c', 'i'), ('d', 'j'), ('e', 'k'), ('f', 'l'), (None, 'm')]

# print(list(zip_longest('abcdef', 'ghijklm', fillvalue='##')))
# [('a', 'g'), ('b', 'h'), ('c', 'i'), ('d', 'j'), ('e', 'k'), ('f', 'l'), ('##', 'm')]


m = [
    [10, 20],
    [30, 40],
    [50, 60],
]

# 3 rows by 2 columns
# (transpose)

pprint(list(zip([10, 20], [30, 40], [50, 60])), width=15)
pprint(list(zip(*m)), width=15)
# how? pprint(list(zip([row for row in m])), width=15)
#pprint(list(zip(x for row in m for x in row)), width=15)
