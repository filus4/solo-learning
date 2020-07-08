def multiply(l):
    result = 1
    for m in l:
        result = result * m
    return result

def persistence(n):
    result = 0
    while True:
        if n > 9:
            digits = [int(x) for x in str(n)]
            n = multiply(digits)
            result += 1
        else:
            return result



print(persistence())