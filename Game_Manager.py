from Card_and_Deck import Card, Deck
from Players_and_Strats import Player, PhaseTracker

class GameManager:
    def __init__ (self, players, deck=None):
        if deck is None:
            deck = Deck()
            deck.populate()
        self.drawpile = deck
        # allows for a nonstandard deck to be passed in for testing

        self.discardpile = Deck()

        self.players = players
        # players requires a list of Player objects to be passed

        self.turn = 0

        self.skip_list = []

        self.round_actions = []
        # (player index, card, action index)

        # actions: discard = 0, draw = 1, play-down = 2
        self.start_round()

    def start_round(self):
        for _ in range(10):
            for player in self.players:
                player.hand.append(self.drawpile.draw())
        self.discardpile.add_card(self.drawpile.draw())

    def shuffle_from_discard(self):
        """takes in all cards from drawpile into discard, then shuffles and makes
        it the new drawpile (does NOT take cards from player hands)"""
        self.discardpile.cards.extend(self.drawpile.cards)
        self.discardpile.shuffle()
        self.drawpile = self.discardpile
        self.discardpile = Deck() 
        

    def tick(self):
        self.player_take_turn()
        self.turn += 1
        self.turn = self.turn % len(self.players)
    
    def player_take_turn(self):
        if self.players[self.turn].draw_from_discard(self.discardpile.tc):
            self.players[self.turn].hand.append(self.discardpile.draw())
        else:
            self.players[self.turn].hand.append(self.drawpile.draw())
        self.players[self.turn].evaluate_hand()
        self.discardpile.add_card(self.players[self.turn].discard_card())


    def endround(self):
        for i in range(len(self.players)):
            self.players[i].tally_points()
            for i in range(len(self.players[i].hand)):
                self.player_discard(i)
                # TODO: ADD IN PLAYERS DISCARDING THE CARDS THAT THEY LAYED DOWN 
        self.shuffle_from_discard()
        
        
    def player_discard(self, pturn = None):
        """takes either a player turn index or uses the current player to take the
        last card from their hand (needs to be called after player sorts hand)"""
        if pturn is None:
            pturn = self.turn
        self.discardpile.add_card(self.players[pturn].discard_card())
    
        
    
        





