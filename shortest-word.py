def find_short(s):
    words = s.split()
    numbers = []
    for shortest in words:
        numbers.append(len(shortest))
    return min(numbers)


def find_short_2(s):
    return min(len(x) for x in s.split())



print(find_short("bitcoin take over the world maybe who knows perhaps"))