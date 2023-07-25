# Implement a algorithm to determine if all the characters on the string are unique

def is_unique_using_array(word):
    occurrecences = [False for _ in range(128)]

    for letter in word:
        asc_value = ord(letter)
        
        if occurrecences[asc_value]:
            return False
        
        occurrecences[asc_value] = True

    return True

print(is_unique_using_array("cas"))