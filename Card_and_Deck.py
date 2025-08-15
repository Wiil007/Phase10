import random

Colors = {"red": 0, "blue": 0, "green": 0,
          "yellow": 0, "wild": 20, "skip": 5}

suites = ["red", "blue", "green", "yellow"]

class Card:
    
    def __init__(self, color, number):
        self.color = color
        self.number = number
        if number >= 10:
            self.value = 10 + Colors[self.color]
        else:
            self.value = 5 + Colors[self.color]
        # worth is a player evaluation of a given card, value is the point value
        # worth should only be set to a non-zero value by Player objects
        self.worth = 0
        
    def __str__(self):
        return f"Color: {self.color}, Number: {self.number}"

class Deck: 

    def __init__(self):
        """Creates a new empty deck (the discard pile is a "deck")"""
        self.cards = []
        # tc = top card
        self.tc = None

    def populate(self):
        # Make 2 coppies of all number cards
        for suite in suites:
            for i in range(1,13):
                self.add_card(Card(suite, i))
                self.add_card(Card(suite, i))
        # Make 8 wilds and 4 skips
        for i in range(8):
            self.add_card(Card("wild", 0))
        for i in range(4):
            self.add_card(Card("skip", 13))
        # shuffle the deck
        self.shuffle()

    def populate_from(self, deck):
        self.cards = deck.cards
        self.tc = deck.tc
    
    def add_card(self, card):
        card.worth = 0
        self.cards.append(card)
        self.tc = card

    def draw(self):
        temp = self.cards.pop()
        self.tc = self.cards[-1]
        return temp
    
    def depopulate(self):
        self.cards = []
        self.tc = None
    
    def shuffle(self):
        random.shuffle(self.cards)
        self.tc = self.cards[-1]
    
    def __str__(self):
        return f"A deck with {len(self.cards)} cards, and \"{self.tc}\" on top"
