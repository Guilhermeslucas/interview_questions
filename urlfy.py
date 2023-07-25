# Write a method that changes the spaces of a string into the char %20.
def urlfy(word, real_size):
    delete_trailing_spaces_word = word[0:real_size]

    new_word = ""
    for letter in delete_trailing_spaces_word:
        if letter == " ":
            new_word += letter
        else:
            new_word += letter

    return new_word

print(urlfy("Mr John Smith                 ", 13))