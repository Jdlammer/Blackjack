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



class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        return self.cards.append(card)
    def get_value(self):
        total = 0
        for i in self.cards:
            total += i




class Deck:
class Play:
class CardLabel:
