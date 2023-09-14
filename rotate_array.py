def rotate_array(numbers, k):
    return numbers[k+1:] + numbers[:k+1]

numbers = [1,2,3,4,5,6,7]
print(rotate_array(numbers, 3))