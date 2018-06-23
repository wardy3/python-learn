from math import fsum, sqrt
from pprint import pprint, pformat
from typing import Iterable, Tuple
from collections import defaultdict
from functools import partial

Point = Tuple[int, ...]


def mean(data: Iterable[float])->float:
    """Accurate arithmetic mean
    """

    data = list(data)

    return fsum(data)/len(data)


def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip)->float:
    """Euclidean distance function for multi-dimensional data
    """

    # print(f"dist p {list(p)} q{list(q)}")

    return sqrt(fsum([(value1-value2)**2 for value1, value2 in zip(p, q)]))


def assign_data(centroids, data):
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(
            centroids, key=partial(dist, point))
        d[closest_centroid].append(point)
    return d


def compute_centroids(groups):
    """Compute the centroid for each group
    """
    print('compute got groups:')
    pprint(groups, width=45)
    return [tuple(map(mean, zip(*group))) for group in groups]


centroids = [(9, 39, 20), (12, 36, 25), ]
print("centroids\n", pformat(centroids))

points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
    (21, 36, 23),
]
print("points\n", pformat(points))

data = assign_data(centroids, points)
print('data returned after assignment is:')
pprint(data, width=45)

print("\nanswer:\n", pformat(compute_centroids(
    [group for group in data.values()])))
