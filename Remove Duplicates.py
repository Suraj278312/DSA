def remove_duplicates(nums):
    # Edge case: empty array
    if len(nums) == 0:
        return 0

    # Pointer for unique element position
    i = 0

    # Traverse the array
    for j in range(1, len(nums)):
        # If current element is different
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    # Length of unique elements
    return i + 1


# Example usage
nums = [1, 1, 2, 2, 3, 4, 4]
new_length = remove_duplicates(nums)

print("Length:", new_length)
print("Array:", nums[:new_length])