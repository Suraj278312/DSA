def single_number(nums):
    result = 0

    for num in nums:
        result = result ^ num

    return result