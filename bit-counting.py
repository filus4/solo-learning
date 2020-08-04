def countBits(n):
    binary = str(bin(n)[2:])
    return binary.count('1')

def count_bits(n):
    return bin(n)[2:].count('1')



number = 1234
print(countBits(number))