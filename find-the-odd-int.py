def find_it(seq):
    seen = {}
    dupes = []
    for x in seq:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    for k, v in seen.items():
        if v % 2 != 0:
            return k


def find_it_2(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i






sequence = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

find_it(sequence)