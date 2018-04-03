# Function to find permutations of a given string
from itertools import permutations

def allPermutations(str):
    perm_list = permutations(str)

    for perm in perm_list:
        print(''.join(perm))

allPermutations('abc')
