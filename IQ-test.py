def iq_test(numbers):
    numbers_list = []
    odd_numbers = []
    even_numbers = []

    for n in numbers.split(' '):
        if (int(n) % 2) == 0:
            even_numbers.append(n)
        else:
            odd_numbers.append(n)
        numbers_list.append(n)

    if len(odd_numbers) == 1:
        return (numbers_list.index(odd_numbers[0]) + 1)
    else:
        return (numbers_list.index(even_numbers[0]) + 1)






test = "2 4 7 8 10"
print(iq_test(test))