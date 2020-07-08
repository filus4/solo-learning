def positive_sum(a):
    positive =[]
    for al in a:
        if al > 0:
            positive.append(al)
    return sum(positive)


list = [1, 6, 8, -5, -1, 2]
positive_sum(list)
