# Go Fish
# Version 1.0
# Compatible with Python 2.7
# June 26, 2017
# by Chris Snyder

# Help in implementing Card, Deck objects comes from
# https://en.wikibooks.org/wiki/Think_Python/Inheritance#Card_objects

import random

from collections import Counter

class Card(object):

    # Playing card

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
			     Card.suit_names[self.suit])

    def compare_rank(self, other_rank_string):
        # Compares card with a rank provided in string
        # print "self.rank equals %s" % Card.rank_names[self.rank]
        # print str(Card.rank_names[self.rank])
        # print "other_rank_string equals %r" % other_rank_string
        # other_rank = self.rank_names.index(other_rank_string)
        # print "other_rank equals %r" % other_rank

        if str(Card.rank_names[self.rank]) == other_rank_string: return 1
        else: return 0

        # could override __cmp__ here
        # and pass in 2 card objects, but we only need a binary yes/no
        # whereas __cmp__ outputs greater than, less than, equal to

class Deck(object):

    # Deck of cards

    def __init__(self):
        self.cards = []
        for suit in range (4):
            for rank in range (13):
                card = Card(suit, rank)
                self.cards.append(card)
        random.shuffle(self.cards)

    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res)

    def deal_card(self):
        return self.cards.pop(0)

class Player(object):

    # Each player in the game

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def __str__(self):
        print ""
        print ""
        print ""
        print "===================================="
        print "Name: %s | Score: %d " % (self.name, self.score)
        print ""
        print "Hand:"
        # Returns each card in the hand, with a newline break between each
        res = [str(card) for card in self.hand]
        return '\n'.join(res)

    # Matches cards if same rank. Returns list of indices.
    def match_card(self, other_rank_string):
        matches = []
        count = 0
        for i in self.hand:
            if i.compare_rank(other_rank_string):
                # print "Found something!"
                matches.append(count)
            else: pass # print "That card didn't match"
            count += 1
        # print matches
	return matches

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def isfour(self):
        # Isolates the ranks from the player's hand
        self.ranks = []
        for j in range (len(self.hand)):
            self.ranks.append(self.hand[j].rank)

        # Uses a Counter to find # of occurrences of each rank
        c = Counter(self.ranks)
        k = c.most_common()
        self.matches = []
        # If a rank occurs 4 times (look in the 2nd half of the tuple)
        # then increment the win counter and make a note of the rank
        for x in k:
            if x[1] == 4:
                print "You have a four-of-a-kind:"
		self.score += 1
		self.matches.append(x[0])
                print str(Card.rank_names[x[0]])
        # print self.matches

        # Now, remove the 4-of-a-kind from the player's hand.
        # I first put the cards to delete in their own list
        self.delete_these_cards = []
        for x in self.hand:
            # print x.rank
            if x.rank in self.matches:
                # print "Found it!"
                self.delete_these_cards.append(x)

        # Then I pass those cards into the delete_cards function
        for i in range (len(self.delete_these_cards)):
            self.remove_card(self.delete_these_cards[i])

        if not self.delete_these_cards: print "You have no 4-of-a-kinds."

        # print self
        

def Turn(player, other_player, deck):

    # Checks if players have cards
    # If all cards gone, signals win condition

    if deck.cards:
        if not player.hand:
            player.add_card(deck.deal_card())
    else:
        print "The deck is empty!"
        return 1

    # Print current status/deck of player
    print player

    # Debug: print other player's status/deck too
    # print other_player

    # Ask player to provide card to ask about
    print ""
    print "Which card do you want to ask your opponent about?"
    rank_to_ask = raw_input("> ")
    print ""

    # At this point, add a "search" method for other_player's hand
    # If the search comes back positive, remove card from
    # other_player's hand and put in your own hand

    # First make sure the player asked about their own card!
    if len(player.match_card(rank_to_ask)) > 0:
        # Then see if the other player has any of that card in their hand.
        other_player_matches = other_player.match_card(rank_to_ask)
	if other_player_matches:
	    print "The other player has a match!"
            # Go through the other player's hand and transfer matching cards to your hand.
            # Traverse the list in reverse order, so when you have
            # multiple matches and you start removing cards,
            # your indices don't get messed up.
	    for i in reversed(other_player_matches):
                #DEBUG print "The index of the other player's card is %r" % i
	        print other_player.hand[i]
                player.add_card(other_player.hand[i])
                other_player.remove_card(other_player.hand[i])
            # Check whether those cards gave you a 4-of-a-kind
            player.isfour()
            # At this point, the turn starts over
            raw_input("Press Enter to continue.")
	    return Turn(player, other_player, deck)
        else:
            print "They didn't have that card!"
            # Draw a card from the deck because the other player didn't have your card.
            draw_card = deck.deal_card()
            player.add_card(draw_card)
	    print "You drew the %s" % draw_card
            # Check whether that card gave you a 4-of-a-kind
            player.isfour()
            if draw_card.compare_rank(rank_to_ask):
	        print "The card you drew matched the card you asked about! Your turn again"
                raw_input("Press Enter to continue.")
                return Turn(player, other_player, deck)
            else:
                print "Next player's turn."
                return 0
            
    else:
        print "Choose a card in your own hand!"
        raw_input("Press Enter to continue.")
        return Turn(player, other_player, deck)

# Splash screen
print ""
print ""
print "=========================="
print "         Go Fish!         "
print "=========================="
print "Version 1.0"
print "Written by Chris Snyder"
print ""
print ""

raw_input("Press Enter to start the game.")

# Initialize game
players = [Player("Player 1"), Player("Player 2")]
deck = Deck()
win = 0
turn_player = 0
other_player = 1

# Debug: print deck
# print deck

# Deal 5 cards to each player
for i in range (5):
    players[0].add_card(deck.deal_card())
    players[1].add_card(deck.deal_card())

# Each player takes turns while the win condition is not met
# and while there are still cards in the deck
while not win:
    win = Turn(players[turn_player], players[other_player], deck)

    if not win:
        turn_player, other_player = other_player, turn_player
        print ""
        raw_input("Pass the computer to the other player, then press Enter.")

# Once win condition happens, tally scores and say who wins

player_1_score = players[0].score
player_2_score = players[1].score

print "Player 1's Score: %d" % player_1_score
print "Player 2's Score: %d" % player_2_score

if player_1_score > player_2_score:
    print "Player 1 wins!"
elif player_2_score > player_1_score:
    print "Player 2 wins!"
else:
    print "Tie game. Good job both players!"


# Debug: See what's in each player's hand
# print players[0]
# print players[1]

# Create a player
# player1 = Player("Chris")
# player2 = Player("Jon")
# print player1
# print player2

# Create a deck, shuffle, and deal a card
# deck = Deck()
# deck.shuffle()
# print deck.cards.__len__()
# print deck.deal_card()
# print deck.cards.__len__()


# Print card
# card1 = Card(2, 11)
# print card1

# Compare cards
# card1 = Card(2, 11)
# card2 = Card(3, 11)
# card3 = Card(2, 10)
# print card1.compare(card2)
# print card1.compare(card3)
# print card2.compare(card3)