def contain_duplicate(numbers):
    occurrence = {}
    for number in numbers:
        if number in occurrence:
            return True
        else:
            occurrence[number] = True
    
    return False

numbers_true = [1,1,1,3,3,4,3,2,4,2]
numbers_false = [1,2,3,4]

print(contain_duplicate(numbers_true))
print(contain_duplicate(numbers_false))