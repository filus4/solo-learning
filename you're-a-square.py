import math

def is_square(n):
    if n > 0:
        sqrt = math.sqrt(n)
        return sqrt.is_integer()
    elif n == 0:
        return True
    elif n < 0:
        return False



number = 16
print(is_square(number))