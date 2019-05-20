#Importing random for deck shuffle
#Importing pyfiglet & colorama for the colorized ASCII title
import random
import pyfiglet
from colorama import Fore, Back, init
#Reseting colorama after each time it is used
init(autoreset=True)


#The Card class is responsible for building each card when the deck class calls it
class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)

#The Deck class is responsible for building the deck, along with other methods such as shuffling and dealing cards. It is capable of dealing a single card
#with _deal(), or dealing a requested number of cards with deal_card(), both of which will remove those cards from the deck pool.
#count() will return the remaining number of cards in the deck.
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

#This function will be called after each time a new card is dealt to both the player or dealer, and will return the total value of their respective hands. 
#This is done for user readability, so they do not have to add the total up themselves.
def card_value(hand):
	values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	total = 0
	for x in hand:
		to_string = str(x)
		card_type = to_string.split(" ",1)[0]
		for value in values:
			if card_type == value:
				if card_type == "A":
					total += 1
				elif card_type == "J":
					total += 11
				elif card_type == "Q":
					total += 12
				elif card_type == "K":
					total += 13
				else:
						total += int(value)
	return total					


#This function will ask the player if they wish to hit or stand, and will continue to ask them if they enter something other than the two options.
#It turns the input into lower case, so that if the player enters a capitilized or uppercase version of the string, it will still accept any variation of it.
def hit_stand():
	choice = input("Hit or Stand?: ")
	choice = choice.lower()

	if choice == "hit" or choice == "stand":
		return choice
	else:
		while not (choice == "hit" or choice == "stand"):
			choice = input("You entered something other than Hit or Stand! Please try again!: ")
			choice = choice.lower()

	return choice

#Initilizing the deck and shuffling the deck.
d = Deck()
d.shuffle()

# Creating the ASCII art and saving it to a variable
header = pyfiglet.figlet_format("BLACKJACK", font="standard")

# Colorizing and printing the ASCII art
print(Fore.WHITE + header)

print("The goal is to get as close to 21 without going over. Dealer stands on 18, Aces are Low. Goodluck!")
print("\n")

#Dealing the first cards to the dealer and player.
player_hand = [d.deal_card()]
print("Player hand: " + str(player_hand) + " Player Total: " + str(card_value(player_hand)))

dealer_hand = [d.deal_card()]
print("Dealer hand: " + str(dealer_hand) + " Dealer Total: " + str(card_value(dealer_hand)))
print("\n")


#
while card_value(player_hand) < 21 and card_value(dealer_hand) < 21:
	choice = hit_stand()
	print("\n")

	if choice == "hit":
		player_hand.append(d.deal_card())
		print("Player hand: " + str(player_hand) + " Player Total: " + str(card_value(player_hand)))

		if card_value(dealer_hand) < 18:
			dealer_hand.append(d.deal_card())
			print("Dealer hand: " + str(dealer_hand) + " Dealer Total: " + str(card_value(dealer_hand)))
			print("\n")

		else:
			print("Dealer Stands with a total of: " + str(card_value(dealer_hand)))
			print("\n")

	else:
		print("Player stands with a total of: " + str(card_value(player_hand)))
		print("\n")
		if card_value(dealer_hand) < 18:
			while card_value(dealer_hand) < 18:
				dealer_hand.append(d.deal_card())
				print("Dealer hand: " + str(dealer_hand) + " Dealer Total: " + str(card_value(dealer_hand)))
				print("\n")

			print("Dealer Stands with a total of: " + str(card_value(dealer_hand)))
			print("\n")
			break
		break


if card_value(player_hand) > 21 and card_value(dealer_hand) > 21:
	print("You both are bust! Nobody wins!")
	print("\n")

elif card_value(player_hand) > 21:
	print("You're bust! Dealer wins!")
	print("\n")

elif card_value(dealer_hand) > 21:
	print("Dealer is bust! You win!")
	print("\n")

elif card_value(player_hand) > card_value(dealer_hand):
	print("Congratulations, you won!")
	print("\n")

elif card_value(dealer_hand) > card_value(player_hand):
	print("The dealer wins!")
	print("\n")
else:
	print("It's a tie!")
	print("\n")