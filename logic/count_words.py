import re

def count_words(str):
    freq = {}
    # list_of_words = str.split(' ')
    list_of_words = re.split((', |; |\* |\s'), str)
    for word in list_of_words:
        # get word count value if exists else 0
        freq[word] = freq.get(word, 0) + 1
    # for word, counter in freq.items():
    return freq

print(count_words('the one; the two one, three four two two'))
