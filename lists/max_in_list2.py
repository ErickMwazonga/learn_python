def max_in_list(lst):
    for i in range(len(lst)):
        largest = lst[i]
        if lst[i+1] > lst[i]:
            largest = lst[i+1]
        else:
            largest = lst[i]
    return largest


print max_in_list([2,3,4,5,6,7,8,8,9,10])
print max_in_list([290,2,3,4])
print max_in_list([9,2,3,4,19])
