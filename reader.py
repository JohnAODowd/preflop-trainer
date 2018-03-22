# Right! Let's start.

from random import choice, shuffle

#print("The Great Game")

path = "hand_orderings.txt"
file = open(path, "r")

def build(file):
    d = { }
    for index, line in enumerate(file, start = 1):
        perc = round(((index / 16432) * 100) + 1)
        if perc not in d:
            d[perc] = []
        d[perc] += [line.strip()]
    return d

def random_val(d):
    values = choice(d)
    key = None
    for k in d:
        if d[k] == values:
            key = k
    return key, choice(values)

def format(str, jumble=False):
	suit_list = ['h', 'd', 'c', 's']
	out = []
	suited = False
	for char in str:
		if char == "(":
			suit = choice(suit_list)
			suited = True
			continue
		elif char == ")":
			suit_list.remove(suit)
			suit = choice(suit_list)
			suited = False
			continue
		elif not suited:
			suit = choice(suit_list)
			suit_list.remove(suit)
		char += suit
		out.append(char)
	if jumble:
		shuffle(out)
	return out

def jumble(card_list):
	jumbled = shuffle(card_list)
	return jumbled

def convert_to_png(card_list):
	for index, card in enumerate(card_list):
		card_list[index] = card + ".png"
	return card_list

rankings = build(file)
value = random_val(rankings)
print("Percentage: %s" % value[0])
print("Hand      : %s" % value[1])
print("Images    : %s" % convert_to_png(format(value[1], jumble=True)))
