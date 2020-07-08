def solve(s, g):

    dif = s - g
    if (dif%g) == 0:
        return (g,dif)
    else:
        return -1