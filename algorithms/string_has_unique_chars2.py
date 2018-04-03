def has_uniques_chars(str):
    if str == None:
        return False

    for char in str:
        if str.count(char) > 1:
            return False
    return True


print(has_uniques_chars('char'))
print(has_uniques_chars('chara'))
