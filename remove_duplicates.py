def remove_duplicates(numbers):
    current_number = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] != current_number:
            current_number = numbers[i]
        else:
            numbers[i] = "_"
    
    return numbers

array = [1,2,2,3,4,5,6,6,7]
print(remove_duplicates(array))