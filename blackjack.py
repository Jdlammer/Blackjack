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
        self.is_hidden = False

    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit
    def get_id(self):
        return self.id
    def is_ace(self):
        return self.rank == 'A'
    def hide(self):
        self.is_hidden = True
    def show(self):
        self.is_hidden = False
    def __str__(self):
        if self.is_hidden:
            return "[?]"
        else:
            return "["+self.rank+" of "+ self.suit+"]"


class Hand:
    def __init__(self):
        self.hand = []
    def add_card(self, card):
        self.hand.append(card)
        return self.hand
    def __str__(self):
        for i in self.hand:
            if i is self.is_hidden:
                return "[?]"
            else:
                return "["+self.rank+ " of " + self.suit+"]"
    def get_value(self):
        total = 0
        for i in self.hand:
            val = i.point
            total += val
        return total
    def get_soft_value(self):
        total = 0
        for i in self.hand:
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
    def __str__(self):
        for i in self.cards:
            return "["+self.rank+ " of " + self.suit+"]"

class Dealer(Hand):
    def __init__(self,name,deck):
        super().__init__(self)
        self.name = name
        self.deck = deck
        self.isBust = False
    def show_hand(self):
        for i in self.hand:
            print (i)
    def hit(self):
        print ("Hit")
        self.add_card(self.deck.deal_card())
        return self.hand
    def stand(self):
        if self.get_value() < 21:
            print ("Stay. You got "+ self.get_value())
        else:
            if self.get_soft_value() < 21:
                print ("Stay. You got "+ self.get_soft_value())
    def bust(self):
        if self.get_soft_value() > 21:
            self.isBust = True
            print ("Busted")
        else:
            self.stand()










class Play:
    myDeck = Deck()
    PlayerHand = Hand()
    DealerHand = Hand()
    in_play = True
    PlayerHand.add_card(myDeck.deal_card())
    DealerHand.add_card(myDeck.deal_card())
    PlayerHand.add_card(myDeck.deal_card())
    DealerHand.add_card(myDeck.deal_card())
    #while in_play:
    if DealerHand.get_value() > PlayerHand.get_value():
        print("You Lose!")
        print(PlayerHand.get_value())
        print(DealerHand.get_value())
    else:
        print("You Win!")
        print(PlayerHand.get_value())
        print(DealerHand.get_value())




