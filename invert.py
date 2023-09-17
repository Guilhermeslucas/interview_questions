def invert_array(array):
    i = 0
    j = len(array) - 1

    while i < j:
        aux = array[i]
        array[i] = array[j]
        array[j] = aux
        i = i + 1
        j = j - 1
    
    return array

array = ["h","e","l","l","o"]
print(invert_array(array))