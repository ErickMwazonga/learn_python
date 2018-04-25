i = 99
while i > 0:
  print """%(b)d %(bo)s of beer on the wall, %(b)d %(bo)s of beer.
Take one down, pass it around, %(lb)d %(lbo)s of beer on the wall.""" % \
  {'b': i, 'lb': i-1, 'bo': 'bottle' if i == 1 else 'bottles', 'lbo': 'bottle' \
  if i == 2 else 'bottles' }
  i -= 1