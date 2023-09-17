def invert_array(number):
    number = list(str(number))
    i = 0
    j = len(number) - 1

    while i < j:
        aux = number[i]
        number[i] = number[j]
        number[j] = aux
        i = i + 1
        j = j - 1
    
    return int("".join(number))

number = 12345
print(invert_array(number))