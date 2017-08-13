# This is a test of the 4-of-a-kind functionality

from collections import Counter
import random

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
        # random.shuffle(self.cards)

    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res)

    def deal_card(self):
        return self.cards.pop(0)

class Player(object):

    def __init__(self):
        self.hand = []

    def __str__(self):
        print "Hand:"
        res = [str(card) for card in self.hand]
        return '\n'.join(res)

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def isfour(self, score):
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
		score += 1
		self.matches.append(x[0])
                print str(Card.rank_names[x[0]])
        print self.matches

        # Now, remove the 4-of-a-kind from the player's hand.
        # I first put the cards to delete in their own list
        self.delete_these_cards = []
        for x in self.hand:
            print x.rank
            if x.rank in self.matches:
                print "Found it!"
                self.delete_these_cards.append(x)

        # Then I pass those cards into the delete_cards function
        for i in range (len(self.delete_these_cards)):
            self.remove_card(self.delete_these_cards[i])

        print self

        return score



player = Player()
deck = Deck()
score = 0

for i in range (52):
    player.add_card(deck.deal_card())

score = player.isfour(score)
