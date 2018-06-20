import random

SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self,rank,suit,id=None):
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
            val = i.point
            total += val
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
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self):
        card = self.cards.pop()
        return card

class Play:
    myDeck = Deck()
    PlayerHand = Hand()
    DealerHand = Hand()
    in_play = True
    PlayerHand.add_card(myDeck.deal_card())
    DealerHand.add_card(myDeck.deal_card())
    PlayerHand.add_card(myDeck.deal_card())
    DealerHand.add_card(myDeck.deal_card())
    DealerHand.add_card(myDeck.deal_card())
    #while in_play:
    if (DealerHand.get_value() or PlayerHand.get_value()) > 21:
        print("You Lose!")
        print(PlayerHand.get_value())
        print(DealerHand.get_value())
    else:
        print("Test")
        print(PlayerHand.get_value())
        print(DealerHand.get_value())




