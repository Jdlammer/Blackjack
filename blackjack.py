import random

SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
class Card:
    def __init__(self,rank,suit,id):
        self.rank = rank
        self.suit = suit
        self.id = id
        if rank == 'A':
            self.point = 11
        elif rank in ['K', 'Q', 'J']:
            self.point = 10
        else:
            self.point = int(rank)
    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit
    def get_id(self):
        return self.id
    def is_ace(self):
        return self.rank == 'A'




class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
        return self.cards
    def get_value(self):
        total = 0
        for i in self.cards:
            total += i
        return total
    def get_soft_value(self):
        total = 0
        for i in self.cards:
            if i.is_ace():
                total += 1
            else:
                total += i
        return total





class Deck:

   def __init__(self):
       self.cards = []
       for suit in SUITS:
           for rank in RANKS:
               self.cards.append(rank,suit)
    def shuffle(self):
        return random.shuffle(self.cards)
class Play:

