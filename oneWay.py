# Given two strings, find out if you can reach the other by doing one edit
def is_one_way_edit_possible(first_word, second_word):
    if first_word == second_word:
        return True
    
    if abs(len(first_word)  - len(second_word) > 1):
        return False

    if len(first_word) == len(second_word):
        return one_way_edit_replace(first_word, second_word)
    else:
        return one_way_edit_insert(first_word, second_word)
    
def one_way_edit_replace(first_word, second_word):
    edited = False

    i = 0 
    while i < len(second_word):
        if first_word[i] != second_word[i]:
            first_word = first_word[:i] + second_word[i] + first_word[i + 1:]
            
            if edited == True:
                return False
            
            edited = True

        i+=1
    
    return True

def  one_way_edit_insert(first_word, second_word):
    if len(first_word) > len(second_word):
        smaller_word = second_word
        bigger_word = first_word
    else:
        smaller_word = first_word
        bigger_word = second_word

    modified = False
    for i in range(0, len(smaller_word)):
        if smaller_word[i] != bigger_word[i]:
            smaller_word = smaller_word[:i] + bigger_word[i] + smaller_word[i:]

            if modified == True:
                return False
            modified = True
    
    return True

# Testing same size words
print(is_one_way_edit_possible("pate", "pat"))