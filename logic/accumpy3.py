def accum(s):
	# enumerate(iterable, start=0)
    for i,j in enumerate(s):
    	if i == len(s)-1:
    		sep = ''
    	else:
    		sep = '-'
        print(j.capitalize()+j*i, end=sep)

accum("abcd")    # "A-Bb-Ccc-Dddd"
# accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt")    # "C-Ww-Aaa-Tttt