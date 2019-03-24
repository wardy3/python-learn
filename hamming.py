from itertools import tee


def times(i, n):
    for x in i:
        yield x*n


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


def generator(inc):
    i = 1
    yield i
    while True:
        i += inc
        yield i


def main():

    for i in range(5):
        for j in range(5):
            for k in range(5):
                print(f"2^{i} 3^{j} 5^{k} = {pow(2,i)*pow(3,j)*pow(5,k)}")

    #     l1 = [x for x in range(10)]
    #     l2 = [x*1.5 for x in range(10)]
    #     i1 = iter(l1)
    #     i2 = iter(l2)

    # print(f"l1 {l1}")
    # print(f"l2 {l2}")

    i1 = generator(1)
    i2 = generator(1.5)
    i3 = times(i2, 2.5)

    # for i in merge(i1, i3):
    #    print(f"i is {i}")


if __name__ == "__main__":
    main()
