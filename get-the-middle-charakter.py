def get_middle(s):
    even = (len(s) // 2)
    if len(s) % 2 == 0:
        return ''.join(s[even - 1 : even + 1])
    else:
        return ''.join(s[even])

def get_middle_2(s):
    even = (len(s) // 2)
    return (''.join(s[even - 1: even + 1]) if len(s) % 2 == 0 else ''.join(s[even]))


print(get_middle('dupson'))