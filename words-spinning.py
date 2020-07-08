def spin_words(sentence):
    result = ''
    for word in sentence.split(' '):
        if len(word) >= 5:
            result += word[::-1] + ' '
        elif len(word) < 5:
            result += word + ' '
    return result.rstrip()

def spin_words_2(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split(' ')])







print(spin_words('Welcome dud how are youuu'))
