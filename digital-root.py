def digital_root(n):
    result = 0
    digits = [int(x) for x in str(n)]
    result += sum(digits)
    while True:
        if result > 9:
            digits = [int(x) for x in str(result)]
            result = sum(digits)
        else:
            return print(result)

def digital_root_2(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n









    print(result)
    print(digits)






digital_root(17221991412516975979679764676444746757657856788)