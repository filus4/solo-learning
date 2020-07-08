def find_outlier(i):
    odd_numbers = []
    even_numbers = []
    for integers in i:
        if integers % 2 == 0:
            even_numbers.append(integers)
        else:
            odd_numbers.append(integers)
    odd_length = len(odd_numbers)
    even_length = len(even_numbers)

    if odd_length > even_length:
        for e_n in even_numbers:
            return print(e_n)
    elif odd_length < even_length:
        for o_n in odd_numbers:
            return print(o_n)

d = [2, 4, 6, 8, 10, 3]

find_outlier(d)
