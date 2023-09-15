def intersection(numbers1, numbers2):
    occurrences1 = {}
    occurrences2 = {}
    intersection = []

    for value in numbers1:
        if value in occurrences1:
            occurrences1[value] = occurrences1[value] + 1
        else:
            occurrences1[value] = 1

    for value in numbers2:
        if value in occurrences2:
            occurrences2[value] = occurrences2[value] + 1
        else:
            occurrences2[value] = 1
    
    for key, value in occurrences1.items():
        if key in occurrences2:
            repetitions = min(value, occurrences2[key])

            intersection = intersection + repetitions * [key]

    return intersection

nums1 = [4,9, 9,5]
nums2 = [9,4,9,8,4]

print(intersection(nums1, nums2))