i = 99
while i > 0:
    print('''
        %(n)d %(np)s of beer on the wall, %(n)d %(np)s of beer.
        Take one down, pass it around, %(l)d %(lo)s of beer on the wall.
        '''
        %{
            'n': i, 'l': i-1,
            'np': 'bottle' if i ==1 else 'bottles',
            'lo': 'bottle' if i == 2 else 'bottles'
        })
    i -= 1
