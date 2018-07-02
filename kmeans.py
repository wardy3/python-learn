from math import fsum, sqrt
from pprint import pprint, pformat
from typing import Iterable, Tuple, List, Sequence, Dict
from collections import defaultdict
from random import sample
from functools import partial

Point = Tuple[int, ...]
Centroid = Point


def mean(data: Iterable[float])->float:
    """ Accurate arithmetic mean
    """

    data = list(data)

    return fsum(data)/len(data)


def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip)->float:
    """ Euclidean distance function for multi-dimensional data
    """

    # print(f"dist p {list(p)} q{list(q)}")

    return sqrt(fsum([(value1-value2)**2 for value1, value2 in zip(p, q)]))


def assign_data(centroids: Sequence[Centroid], data: Iterable[Point])-> Dict[Centroid, List[Point]]:
    """ Group the data points to their closest centroid
    """

    d = defaultdict(list)
    for point in data:
        closest_centroid = min(
            centroids, key=partial(dist, point))
        d[closest_centroid].append(point)
    return dict(d)


def compute_centroids(groups: Iterable[Sequence[Point]])->List[Centroid]:
    """ Compute the centroid for each group
    """
    print('compute got groups:')
    pprint(groups, width=45)
    return [tuple(map(mean, zip(*group))) for group in groups]


def k_means(data: Iterable[Point], k: int=2, iterations: int=50)->List[Centroid]:
    data = list(data)
    centroids = sample(data, k)
    labeled = assign_data(centroids, data)
    print(f"labeled {pformat(labeled)}")
    centroids = compute_centroids(labeled.values())
    print(f"centroids {pformat(centroids)}")
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        print(f"labeled {i} {pformat(labeled)}")
        centroids = compute_centroids(labeled.values())
        print(f"centroids {i} {pformat(centroids)}")
    return centroids


points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
    (21, 36, 23),
]


def main():
    print("points\n", pformat(points), "\n")

    centroids = k_means(points, k=2)
    d = assign_data(centroids, points)
    pprint(d, width=45)


if __name__ == '__main__':
    main()
