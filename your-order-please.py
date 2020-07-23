import re

def order(sentence):
    return ' '.join(sorted(sentence.split(' '), key=get_order) if sentence else "")



def get_order(word):
    number_pattern = re.compile(r'\d')
    number_pattern_match = number_pattern.search(word)
    return word[number_pattern_match.start(): number_pattern_match.end()]





s = "4of Fo1r pe6ople g3ood th5e the2"
print(order(s))
