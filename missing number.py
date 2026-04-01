def missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2

    array_sum = 0
    for num in nums:
        array_sum += num

    return total_sum - array_sum