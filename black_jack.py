import random

turn = 0

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
		if card.value == 'As':
			self.ace = True
		self.value += score[card.value]

class Player(object):
	def __init__(self, bankroll = 100, name = 'Dealer', showed = True, lost = False):
		self.bet = 0
		self.bankroll = bankroll
		self.name = name
		self.showed = showed
		#associate a hand classes to the player
		self.hand = Hand()
		self.lost = lost

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
		for i in range(7):
			for color in colors:
				for value in values:
					self.deck.append(Card(color,value))

	def shuffle(self):
		random.shuffle(self.deck)

class Game(object):
	def __init__(self):
		self.turn = 0
		self.deck = Deck()
		self.deck.shuffle()
		new_game = 'Hey, how many players do we have ?\n'
		self.nb_players = input(new_game)

		#creates a list of players according to the numbers of players we have
		self.players = []
		for i in range(self.nb_players):
			name = str(raw_input('What is your name, player ' + str(i + 1) + '?\n'))
			bankroll = int(raw_input('How many coins do you want to play ' + name + '?\n'))
			self.players.append(Player(bankroll = bankroll, name = name))

		#add the last player, who is the dealer
		self.players.append(Player(name = 'Dealer', showed = False))






def deal(game):
	#deals 2 cards to each players including the dealer
	for id_card in range(0, 2):
		for i in range(game.nb_players + 1):
			game.players[i].hand.card_add(game.deck.deck[game.deck.count])
			game.deck.count += 1
			game.players[i].hand.nb_cards += 1

def show_card(game):
	#display a list of cards and score that all the players have
	for i in range(0, game.nb_players + 1):
		print game.players[i].name + ' you have :'
		print game.players[i].hand.cards[0].value + ',' + game.players[i].hand.cards[0].color

		#we dont want to display the 2nd card of the dealer
		if game.players[i].showed == True:
			print game.players[i].hand.cards[1].value + ',' + game.players[i].hand.cards[1].color
			print game.players[i].hand.value
		else:
			print ('(Hidden)')

def play_dealer(game, dealer):
	print 'The dealer has ' + dealer.hand.cards[0].value + ',' + dealer.hand.cards[0].color + '\n' + \
	dealer.hand.cards[1].value + ',' + dealer.hand.cards[1].color
	print 'Score : ' + str(dealer.hand.value)
	while dealer.hand.value < 16:
		print 'Drawing...'
		dealer.hand.card_add(game.deck.deck[game.deck.count])
		print game.deck.deck[game.deck.count].value + ', ' + game.deck.deck[game.deck.count].color
		game.deck.count += 1
		print 'The dealer has now \n' + dealer.hand.cards[0].value + ',' + dealer.hand.cards[0].color + '\n' + \
		dealer.hand.cards[1].value + ',' + dealer.hand.cards[1].color
		print 'Score : ' + str(dealer.hand.value)

def play_turn(game, dealer):
	for i in range(game.nb_players):
		move = raw_input('Hey '+ game.players[i].name + ' your score is: ' + \
		str(game.players[i].hand.value) + ' what is your move ? Press H for hit or S to stand\n')
		while move == 'h' and game.players[i].hand.value < 21:
			game.players[i].hand.card_add(game.deck.deck[game.deck.count])
			print game.deck.deck[game.deck.count].value + ', ' + game.deck.deck[game.deck.count].color
			game.deck.count += 1
			move = raw_input('Now, '+ game.players[i].name + 'your score is: ' + \
			str(game.players[i].hand.value) + ' what is your move ? Press H for hit or S to stand\n')
		if game.players[i].hand.value > 21:
			game.players[i].bankroll -= game.players[i].bet
			print 'Burn ! You lost your bet'
			print 'You have now ' + str(game.players[i].bankroll) + 'coins'
			game.players[i].lost = True
	play_dealer(game, dealer)
	if dealer.hand.value > 21:
		print 'The dealer burned !'
	for j in range(game.nb_players):
		if dealer.hand.value > 21:
			if game.players[j].lost == False:
				game.players[j].bankroll += game.players[j].bet
				print game.players[j].name + ' you won against the dealer'
				print 'You have now ' + str(game.players[j].bankroll) + 'coins'
		elif dealer.hand.value > game.players[j].hand.value or game.players[j].lost == True:
			game.players[j].bankroll -= game.players[j].bet
			print game.players[j].name + ' you lost your bet against the dealer'
			print 'You have now ' + str(game.players[j].bankroll) + 'coins'
		else :
			game.players[j].bankroll += game.players[j].bet
			print game.players[j].name + ' you won against the dealer'
			print 'You have now ' + str(game.players[j].bankroll) + 'coins'
	game.turn += 1

def get_bets(game):
	for i in range(game.nb_players):
		correct = False
		while correct == False:
			amount = input('What is your bet for this turn '+ game.players[i].name +'?')
			if amount > game.players[i].bankroll:
				print 'You dont have enough coins, try again'
			else:
				game.players[i].bet = amount
				correct = True

def ajust_players(game):
	for i in range(game.nb_players):
		del game.players[i].hand
		game.players[i].hand = Hand()
		replay = raw_input('Do you want to play again ' + game.players[i].name + '? (y/n)')
		if (replay == 'n'):
			print 'Alright goodbye ' + game.players[i].name
			game.players.pop(i)
			game.nb_players -= 1


def play_game(game, dealer):
	while game.nb_players > 0:
		deal(game)
		get_bets(game)
		show_card(game)
		play_turn(game, dealer)
		if game.turn > 0:
			ajust_players(game)


game = Game()
dealer = game.players[-1]
play_game(game, dealer)
