'''
Write a function that takes a list of float numbers
and return the sum of their digits.
e.g [10.5, 6, 8.2] = 1+0+5+6+8+2 = 22
'''

def super_sum_revised(a):
    sum_ = 0
    for i in a:
        i = str(i)
        if '.' in i:
            i = i.replace('.', '')
        for j in i:
            sum_ += int(j) 
    return sum_

print super_sum_revised([10.5, 6, 8.2])