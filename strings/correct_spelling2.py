def correct(str):
    remove_in_between_spaces = re.sub(r'\s{2,}', ' ', str)
    remove_space_before_period = re.sub(r'\s+(?=\.)', '', remove_in_between_spaces)
    add_space_after_period = re.sub(r'(\.)(\w)', r'\1 \2', remove_space_before_period)
    result = add_space_after_period
    return result

print(correct('This   is        very funny  and    cool .Indeed!'))
