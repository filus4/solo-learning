import string

def alphabet_position(text):
    alphabet = {}
    text = text.lower()
    result = ''
    for word in string.ascii_lowercase:
        alphabet[word] = (ord(word) - 96)
    for letter in text:
        for k, v in alphabet.items():
            if letter == k:
                result += str(v) + ' '
    return result.rstrip()

def alphabet_position_2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


alphabet_position("The sunset sets at twelve o' clock.")





alphabet_position('bla bla bla')


