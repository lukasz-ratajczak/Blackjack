import random
from Card import Card

suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:
    sec_deck = []

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        for num in self.deck:
            print(num)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) < 1:
            self.deck += self.sec_deck
            self.sec_deck = []
            random.shuffle(self.deck)
        single_card = self.deck.pop()
        self.sec_deck.append(single_card)
        return single_card
