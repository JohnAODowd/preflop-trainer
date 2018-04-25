from random import choice, shuffle

def build(file):
    d = { }
    num_lines = file_len(file)
    file.seek(0)
    for index, line in enumerate(file, start = 1):
        perc = round(((index / num_lines) * 100) + 1)
        if perc not in d:
            d[perc] = []
        d[perc] += [line.strip()]
    return d

def file_len(file):
    file.seek(0)
    for i, l in enumerate(file, start = 1):
        pass
    return i

def random_val(d):
    values = choice(d)
    key = None
    for k in d:
        if d[k] == values:
            key = k
    return key, choice(values)

def convert_to_png(card_list):
    for index, card in enumerate(card_list):
        card_list[index] = card + ".png"
    return card_list
