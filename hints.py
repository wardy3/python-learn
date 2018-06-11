from typing import *
from collections import OrderedDict, deque, namedtuple
import secrets

x = 10  # type: int
z: int = 20


def f(x: int, y: Optional[int]=None) -> int:
    if y is None:
        y = 20
    return x+y


print(f"f(10,20) returns {f(10, 20)}")
print('f', f(20))


y = OrderedDict()  # type: OrderedDict


def g(x: List[int]) -> None:
    print('len', len(x))
    print('el 2', x[2])
    for i in x:
        print('i', i)
    print()


g([10, 20, 30])
# g('abcdef')
#g((11, 12, 13))
# g(None)

hts = [97, 1, 102.5, 97.5]      # type: List[float]
person = ('Raymond', 5*12+11)   # type: Tuple[str,float]
info = ('Pearson', 'Course', 'Python', 'Raymond')  # type: Tuple[str,...]

Point = NamedTuple('Point', [('x', int), ('y', int)])
vars(Point)

# TODO error checking
#   mypy
#   pyflakes
#   hypothesis
#   unittest -> nose py.test
