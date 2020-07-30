def is_valid_walk(walk):
    x_axis = 0
    y_axis = 0
    if len(walk) == 10:
        for w in walk:
            if w == 'n':
                y_axis += 1
            elif w == 's':
                y_axis -= 1
            elif w == 'e':
                x_axis += 1
            elif w == 'w':
                x_axis -= 1
        result = f'{x_axis},{y_axis}'
    else:
        return False
    if result == '0,0':
        return True
    else:
        return False


def is_valid_walk_2(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


path = ['n','s','n','s','n','s','n','s','n','s','w']
path_2 = ['e', 's', 'e', 'w', 'w', 'n', 'w', 'e']
print(is_valid_walk(path_2))