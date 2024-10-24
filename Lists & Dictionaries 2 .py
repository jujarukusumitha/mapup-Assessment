def group_by_length(strings):
    length_dict = {}

    # Iterate over each string in the list
    for s in strings:
        length = len(s)  # Get the length of the string

        # If the length is not a key in the dictionary, create a new list for it
        if length not in length_dict:
            length_dict[length] = []

        # Append the string to the list corresponding to its length
        length_dict[length].append(s)

    # Sort the dictionary by its keys (string lengths)
    return dict(sorted(length_dict.items()))

# Test cases
print(group_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))
# Output: {3: ['bat', 'car', 'dog'], 4: ['bear'], 5: ['apple'], 8: ['elephant']}

print(group_by_length(["one", "two", "three", "four"]))
# Output: {3: ['one', 'two'], 4: ['four'], 5: ['three']}
