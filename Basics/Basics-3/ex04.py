import itertools

listOfElements = [
    'element-1',
    'element-2',
    'element-3',
    'element-4',
]
permutations = list(itertools.permutations(listOfElements))

for item in permutations:
    print(item)

#You can also specify the length of the permutations using the 'r' argument
# of the 'permutations()' function.

permutations = list(itertools.permutations(listOfElements, r=2))

for item in permutations:
    print(item)