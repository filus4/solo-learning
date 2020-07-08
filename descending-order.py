def descending_order(num):
    numbers = [int(descending) for descending in str(num)]
    result = ''.join(str(digit) for digit in reversed(sorted(numbers)))
    return int(result)


print(descending_order(123456789))