# Write a method that, given two strings, decide if one is a permutation of the other
def is_permutation(first_word, second_word):
    if len(first_word) != len(second_word):
        return False
    
    if first_word == second_word:
        return True
    
    sorted_first_word = sorted(first_word)
    sorted_second_word = sorted(second_word)

    return sorted_first_word == sorted_second_word

print(is_permutation("asa", "aaa"))