def max_diff(array):
    min_value = array[0]
    max_diff = 0
    
    for i in range(1, len(array)):
        if array[i] - min_value > max_diff:
            max_diff = array[i] - min_value

        if array[i] < min_value:
            min_value = array[i]

    return max_diff

print(max_diff([1, 2, 6, 80, 100]))