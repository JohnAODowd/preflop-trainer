from random import choice, shuffle

str = 'T(98)7'

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

print(format(str))
print(format(str, jumble=True))




