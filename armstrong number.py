def is_armstrong(n):
    num = n
    digits = 0

    temp = n
    while temp > 0:
        digits += 1
        temp = temp // 10

    sum = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp = temp // 10

    if sum == num:
        return True
    else:
        return False