def duplicate_count(text):
    seen = {}
    duplicates = 0
    for i in text.lower():
        if i not in seen:
            seen[i] = 1
        else:
            if seen[i] == 1:
                duplicates += 1
            seen[i] += 1

    return print(duplicates)






duplicate_count("aAbcdefg")