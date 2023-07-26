# find out if, given a word, its a permutation of a palindrome
def is_palindrome_permutation(word):
    occurrences = [False for _ in range(128)]

    for letter in word:
        asc_value = ord(letter)
        
        if occurrences[asc_value] == True:
            occurrences[asc_value] = False
        else:
            occurrences[asc_value] = True

    odd_count = 0
    for value in occurrences:
        if value == True:
            odd_count += 1
    
    if odd_count > 1:
        return False
    if odd_count == 0:
        return True
    if odd_count == 1 and len(word) % 2 == 1:
        return True
    
print(is_palindrome_permutation("tactcoa"))