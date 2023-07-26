# define if a string is a substring of the other
def is_substring(word, substring_candidate):
    if word == substring_candidate:
        return True
    
    word += word

    return substring_candidate in word

print(is_substring("erbottlewat", "waterbottle"))