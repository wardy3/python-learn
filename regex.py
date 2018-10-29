import re

string = 'match some crap out of here please'

num_name = re.compile(r'''
    (\d*)
    \s*
    (\w+)
    ''', re.VERBOSE)

groups = num_name.search(string)

print(groups)


# a, b = groups(1, 2)

# print(f'a is {a}\tb is {b}')
