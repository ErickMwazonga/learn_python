def check_freg(str):
    freq = {}
    for c in str:
        freq[c] = str.count(c)
    return freq

print(check_freg("abbabcbdbabdbdbabababcbcbab"))
# {'a': 7, 'b': 14, 'c': 3, 'd': 3}
