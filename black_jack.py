import random

colors = ('Heart', 'Diamond', 'Clover', 'Pike')

values = ('As', '2', '3', '4', '5', '6', '7', '8','9','10','Jack', 'Queen', 'King')


class Player(object):
	def __init__(self, bankroll = 100, name = 'Dealer'):
		self.bankroll = bankroll
		self.name = name

	def change_bankroll(self, amount):
		self.bankroll += amount

	def get_name(self):
		return self.name

	def get_bankroll(self):
		return self.bankroll

class Card(object):
	def __init__(self, color, value):
		self.color = color
		self.value = value

	def get_value(self):
		return self.value

	def get_color(self):
		return self.color

class Deck(object):
	def __init__(self):
		self.deck = []
		for color in colors:
			for value in values:
				self.deck.append(Card(color,value))

	def shuffle(self):
		random.shuffle(self.deck)

class Hand(object):
	def __init__(self, card1, card2, nb_cards = 0):
		self.card1 = card1
		self.card2 = card2


def deal(deck, players, nb_players):
	pass



deck = Deck()
deck.shuffle()
new_game = 'Hey, how many players do we have ?\n'
nb_players = input(new_game)
players = [None] * (nb_players + 1)
for i in range(nb_players):
	name = str(raw_input('What is your name, player ' + str(i + 1) + '?\n'))
	bankroll = int(raw_input('How many coins do you want to play ' + name + '?\n'))
	players[i] = Player(bankroll = bankroll, name = name)
players[nb_players] = Player(name = 'Dealer')

deal(deck, players, nb_players)
