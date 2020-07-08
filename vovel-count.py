def get_count(input_str):
    num_vowels = 0

    for i_s in input_str:
        if 'e' in i_s:
            num_vowels += 1
        elif 'a' in i_s:
            num_vowels += 1
        elif 'i' in i_s:
            num_vowels += 1
        elif 'o' in i_s:
            num_vowels += 1
        elif 'u' in i_s:
            num_vowels += 1

    return print(num_vowels)


def get_count_2(input_str):
    num_vowels = 0

    for char in input_str:
        if char in "aeiouAEIOU":
            num_vowels += 1
    return print(num_vowels)


def get_count_3(input_str):
    return sum(input_str.count(char) for char in ['a', 'e', 'i', 'o', 'u'])


derp = "o a kak ushakov lil vo kashu kakao"
get_count(derp)
get_count_2(derp)
get_count_3(derp)