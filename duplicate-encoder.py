def duplicate_encode(string):
    string = string.lower()
    seen = {}
    result = ''
    for i in string:
        seen[i] = string.count(i)
        if seen[i] == 1:
            result += '('
        elif seen[i] > 1:
            result += ')'
    return result


def duplicate_encode_2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])



print(duplicate_encode('(( @'))