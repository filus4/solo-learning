def high_and_low(n):
    number = [int(x) for x in n.split()]
    return f'{max(number)} {min(number)}'








print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
