def square_digits(number):
    result = ''
    for numbers in str(number):
        result += str(int(numbers) ** 2)
    return int(result)

def square_digits_2(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits(21321))