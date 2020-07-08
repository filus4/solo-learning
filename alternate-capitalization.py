def capitalize(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]


def capitalize_2(s):
    word = ''
    output = []

    for n in range(0, len(s)):
        if n % 2 == 0:
            word = word+s[n].upper()
        else:
            word = word + s[n]
    output.append(word)
    output.append(word.swapcase())

    return output

print(capitalize_2('dupa jasia stasia'))

