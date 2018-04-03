list = range(0, 10)

for i in list:
    if list[i] == list[-1]:
        print(i)
    else:
        print(i, end=', ')
