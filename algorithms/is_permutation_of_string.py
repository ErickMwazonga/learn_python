'''
Write a program that check whether one string is a permutation of another.
One or more None inputs -> False
One or more empty strings -> False
'Nib', 'bin' -> False
'act', 'cat' -> True
'a ct', 'ca t' -> True
'dog', 'doggo' -> False
'''

def is_permutation(str1, str2):
    if str1 is None or str2 is None:
        return False
    return sorted(str1) == sorted(str2)


print(is_permutation('cat', 'act'))
print(is_permutation('cat', 'acft'))
