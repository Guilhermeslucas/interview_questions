# Implement a simple encoding algorithm
def encode_string(word):
    encoded_string = ""

    current_letter = word[0]
    current_count = 1

    for letter in word[1:]:
        if letter != current_letter:
            encoded_string += current_letter + str(current_count)
            current_letter = letter
            current_count = 1
        else:
            current_count += 1
    
    encoded_string += current_letter + str(current_count)
    
    return encoded_string

print(encode_string("aabcccccaaa"))