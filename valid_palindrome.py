def is_valid_palindrome(sentence):
    filtered_sentence = sentence.replace(" ", "").replace(",","").replace(":","")

    i = 0
    j = len(filtered_sentence) - 1

    while i < j:
        if filtered_sentence[i] != filtered_sentence[j]:
            return False
        i = i + 1
        j = j - 1

    return True

sentence = "a man, a plan, a canal: panama"
print(is_valid_palindrome(sentence))