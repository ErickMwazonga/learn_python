def has_uniques_chars(str):
    if str is None:
        return False
    return len(set(str)) == len(str)


print(has_uniques_chars('char'))