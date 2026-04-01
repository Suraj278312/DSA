def highest_frequency(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_count = 0
    element = None

    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            element = key

    return element, max_count