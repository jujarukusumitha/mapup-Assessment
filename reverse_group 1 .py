def reverse_in_groups(lst, n):
    result = []
    
    # Iterate over the list in chunks of size 'n'
    for i in range(0, len(lst), n):
        group = []
        # Find the actual size of the group (either 'n' or remaining elements)
        actual_group_size = min(n, len(lst) - i)
        
        # Manually reverse the group of 'n' elements or fewer
        for j in range(actual_group_size):
            group.append(lst[i + actual_group_size - 1 - j])
        result.extend(group)
    
    return result

# Test cases
print(reverse_in_groups([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [3, 2, 1, 6, 5, 4, 8, 7]
print(reverse_in_groups([1, 2, 3, 4, 5], 2))           # Output: [2, 1, 4, 3, 5]
print(reverse_in_groups([10, 20, 30, 40, 50, 60, 70], 4))  # Output: [40, 30, 20, 10, 70, 60, 50]
