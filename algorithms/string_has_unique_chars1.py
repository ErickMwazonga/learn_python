def has_uniques_chars(str):
    if str == None:
        return False

    char_set = set()
    for char in str:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True


print(has_uniques_chars('char'))
print(has_uniques_chars('chara'))
