import random

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(value, suit) for suit in suits for value in values]

	def __repr__(self):
		return "Deck of " + str(self.count()) + " cards"

	def count(self):
		return len(self.cards)

	def _deal(self, num):
		count = self.count()
		actual = min([count,num])
		if count == 0:
			raise ValueError ("All cards have been dealt!")
		hand = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return hand

	def shuffle(self):
		count = self.count()
		if count < 52:
			raise ValueError("Only full decks can be shuffled")
		else:
			shuffled = self.cards
			random.shuffle(shuffled)
			return shuffled

	def deal_card(self):
		single_card = self._deal(1)[0]
		return single_card

	def deal_hand(self, num):
		num = num
		new_hand = self._deal(num)
		return new_hand