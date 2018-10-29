from collections import defaultdict

e = defaultdict(set)
e['t'].add('tom')
e['m'].add('mary')
e['m'].add('martha')


names = '''david betty susan mary darlene sandy davin
           shelly becky beatrice tom nicahel wallace'''.split()

d = defaultdict(list)
for name in names:
    #feature = name[0]
    #feature = name[-1]
    feature = len(name)
    d[feature].append(name)

from pprint import pprint

pprint(d)


# SELECT name FROM names ORDER BY len(name);
pprint(sorted(names, key=len))
