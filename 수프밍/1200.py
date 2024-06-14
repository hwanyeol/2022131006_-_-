def calculate_absolute_differences(lst):
    absolute_diff_dict = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            difference = abs(lst[i] - lst[j])
            if difference not in absolute_diff_dict:
                absolute_diff_dict[difference] = []
            absolute_diff_dict[difference].append([min(lst[i], lst[j]), max(lst[i], lst[j])])

    sorted_keys = sorted(absolute_diff_dict.keys())
    
    result = []
    for key in sorted_keys:
        result += absolute_diff_dict[key]

    return result

example_list = [2, 4, 7, 1, 9]
result = calculate_absolute_differences(example_list)
print(result)
