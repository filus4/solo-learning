def create_phone_number(n):
    result = ''.join(str(number) for number in n)
    return ''.join(f'({result[0:3]}) {result[3:6]}-{result[6:]}')





phone_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(phone_number))