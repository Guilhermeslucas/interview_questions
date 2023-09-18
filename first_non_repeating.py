def first_non_repeating(input_string):
    ocurrences = {}

    for i in range(len(input_string)):
        if input_string[i] in ocurrences:
            ocurrences[input_string[i]] = (2, i)
        else:
            ocurrences[input_string[i]] = (1, i)

    min_index = len(input_string) + 1

    for key, value in ocurrences.items():
        if value[0] == 1 and min_index > value[1]:
            min_index = value[1]

    return min_index

input_string = "leetcode"
print(first_non_repeating(input_string))