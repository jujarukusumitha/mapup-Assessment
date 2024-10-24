def unique_permutations(nums):
    result = []
    nums.sort()  # Sort the list to ensure duplicates are handled
    used = [False] * len(nums)

    def backtrack(current_permutation):
        # If current permutation is complete, add it to the result
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])
            return
        
        for i in range(len(nums)):
            # Skip duplicates by ensuring we only take the first instance
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            
            # Mark the number as used and continue backtracking
            used[i] = True
            current_permutation.append(nums[i])
            backtrack(current_permutation)
            # Backtrack: remove the number and mark it as unused
            current_permutation.pop()
            used[i] = False
    
    backtrack([])
    return result

# Test case
nums = [1, 1, 2]
unique_perms = unique_permutations(nums)
print(unique_perms)
