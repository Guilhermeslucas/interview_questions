def move_zeros(numbers):
    zeros_count = 0
    
    i = 0
    while i < len(nums):
        if numbers[i] == 0:
            zeros_count = zeros_count + 1
            del nums[i]
        else:
            i = i + 1 
    
    return numbers + zeros_count * [0]

nums = [0,1,0,3,12]
print(move_zeros(nums))