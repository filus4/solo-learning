def disemvowel(string):
    words = ['a','e','i','o','u','A','E','I','O','U']
    for charakters in words:
        string = string.replace(charakters,'')
    return string


print(disemvowel('ale bekA z cb gościU wgle ciota hahah ale lamus'))