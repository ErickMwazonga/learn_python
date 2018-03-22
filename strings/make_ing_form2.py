def make_ing_form(verb):
    vowels = 'aeiou'
    if verb.endswith('ie'):
        return verb[:-2]+'ying'
    elif verb.endswith('e'):
        return verb[:-1]+'ing'
    elif verb.endswith('ie'):
        return verb[:-2]+'ying'
    elif(len(verb) == 3) and (verb[0] not in vowels) and (verb[1] in vowels) and (verb[2] not in vowels) :
        return verb + verb[2] + 'ing'
    else:
        return verb+'ing'


print(make_ing_form('lie'))
print(make_ing_form('see')) # I know. Doesn't work. It's an exception
print(make_ing_form('move'))
print(make_ing_form('hug'))
print(make_ing_form('touch'))
