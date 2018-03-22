def longest_word(lst):
    longest = len(lst[0])
    for i in lst:
        if len(i) > longest:
            longest = len(i)
    return longest

print(longest_word(['hello', 'world', 'Python']))
print(longest_word(['Live', 'laugh', 'love']))
print(longest_word(['I', 'found', 'Haiti']))
