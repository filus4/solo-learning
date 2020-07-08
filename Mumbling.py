def accum(s):
    result = s[0]
    for i in range(1, len(s)):
        letter = s[i] * (i+1)
        result += f'-{letter}'

    res = result.split('-')
    result = '-'.join([x[0].upper() + x[1:].lower() for x in res])

    return result


def accum_2(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))





print(accum('abcdmTny'))