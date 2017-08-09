import random

colors = ('Heart', 'Diamond', 'Clover', 'Pike')

values = ('As', '2', '3', '4', '5', '6', '7', '8','9','10','Jack', 'Queen', 'King')

score = {'As': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,'9': 9, \
'10': 10,'Jack': 10,'Queen': 10, 'King': 10}

class Hand(object):
	def __init__(self, card1 = None, card2 = None, nb_cards = 0):
		self.cards = []
		self.nb_cards = nb_cards
		self.value = 0

	def card_add(self,card):
		''' Add another card to the hand'''
		self.cards.append(card)

	# Check for Aces
		if card.value == 'A':
			self.ace = True
		self.value += score[card.value]

class Player(object):
	def __init__(self, bankroll = 100, name = 'Dealer', showed = True):
		self.bankroll = bankroll
		self.name = name
		self.showed = showed
		#associate a hand classes to the player
		self.hand = Hand()

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
	count = 0
	'''
	add here a condition when count > nb cards
	'''
	def __init__(self):
		self.deck = []
		for color in colors:
			for value in values:
				self.deck.append(Card(color,value))

	def shuffle(self):
		random.shuffle(self.deck)


def deal(deck, players, nb_players):
	#deal 2 cards to each players including the dealer
	while players[nb_players].hand.nb_cards < 2:
		for id_card in range(0, 2):
			for i in range(nb_players + 1):
				players[i].hand.card_add(deck.deck[deck.count])
				deck.count += 1
				players[i].hand.nb_cards += 1

def show_card(players, nb_players):
	#display a list of cards and score that all the players have
	for i in range(0, nb_players + 1):
		print players[i].name + ' you have :'
		print players[i].hand.cards[0].get_value() + ',' + players[i].hand.cards[0].get_color()

		#we dont want to display the 2nd card of the dealer
		if players[i].showed == True:
			print players[i].hand.cards[1].get_value() + ',' + players[i].hand.cards[1].get_color()
			print players[i].hand.value
		else:
			print ('(Hidden)')

deck = Deck()
deck.shuffle()
new_game = 'Hey, how many players do we have ?\n'
nb_players = input(new_game)

#creates a list of players according to the numbers of players we have
players = []
for i in range(nb_players):
	name = str(raw_input('What is your name, player ' + str(i + 1) + '?\n'))
	bankroll = int(raw_input('How many coins do you want to play ' + name + '?\n'))
	players.append(Player(bankroll = bankroll, name = name))

#add the last player, who is the dealer
players.append(Player(name = 'Dealer', showed = False))

deal(deck, players, nb_players)
show_card(players, nb_players)
