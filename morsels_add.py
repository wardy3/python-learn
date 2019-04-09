"""
I'd like you to write a function that accepts two lists-of-lists of numbers
and returns one list-of-lists with each of the corresponding numbers in the
two given lists-of-lists added together.

It should work something like this:
>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

"""


def add(*lists_of_lists) -> list:
    added = []
    # print(list(zip(*list_of_lists)))
    for m in zip(*lists_of_lists):
        # print(f"m {m}")
        # print(f"lens {set([len(x) for x in m])}")
        if len(set([len(x) for x in m])) != 1:
            raise ValueError("Given matrices are not the same size.")
        added.append([sum(x) for x in zip(*m)])
    return added


# def two_add(list_of_list1, list_of_list2) -> list:
#     added = []
#     for m1, m2 in zip(list_of_list1, list_of_list2):
#         # print(list((zip(m1, m2))))
#         # added.append(sum(zip(m1, m2)))
#         added.append([sum(x) for x in zip(m1, m2)])
#     return added

if __name__ == "__main__":
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print(add(matrix1, matrix2))

    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    print(add(matrix1, matrix2))

    print(add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]]))
    # [[8, 8], [7, 7]]

    print(add([[1, 9], [7]], [[1, 2], [3]]))
    print(add([[1, 9], [3]], [[1, 2], [3, 9]]))
