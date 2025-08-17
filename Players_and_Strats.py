from Card_and_Deck import Card, Deck

class Player:
    def __init__(self, agression, randomness):
        # agression determines how much the player values harming others 
        # ie. playing a skip at the start to hurt the leading player
        # scale from 0-x
        self.agro = agression

        # randomness is a measure of exactly that, how often they pick randomly
        # scale from 0-x
        self.randomness = randomness

        # player hand
        self.hand = []

        self.played_down = False
        # ph
        self.points = 0
        self.phase = 1

        # this is a temporary stand in for the tuple that comes based on self.phase
        self.phase_part_1 = set_of_cards(3)
        self.phase_part_2 = set_of_cards(3)

    # def draw_card_from(self, deck):
    #     self.hand.append(deck.draw())
    
    def discard_card(self):
        """THE DISCARD FUNCTION ONLY WORKS AFTER BEING SORTED BY WORTH, OR AT GAME END"""
        
        card = self.hand.pop()
        card.worth = 0
        return card
    
    def tally_points(self):
        for card in self.hand:
            self.points += card.value

    def take_turn(self, tc_discard):
        pass
        
    def __str__(self):
        hand = "---\n"
        for card in self.hand:
            hand += str(card) + "\n"
        return hand
    
    def sort_hand(self):
        self.hand.sort(key=lambda card: -1*card.worth)
    
    def give_sorted_hand_by_number(self):
        """returns copy of hand sorted by number (decending) without skips"""
        self.hand.sort(key=lambda card: -1*card.number)
        return [c for c in self.hand if c.number != 13]

    def draw_from_discard(self, card):
        """evaluates discard pile card (in context of hand) and draw pile card (based on known cards)
        and outputs false (draw pile) or true (discard pile) to draw from"""
        pass

    def evaluate_hand(self):
        """takes in the hand and information from game manager, checks if play is possible, 
        then orders hand with last card as the one to discard"""
        pass

    def can_play_down(self):
        sorted_hand = self.give_sorted_hand_by_number()
        phases = [(self.phase_part_1,self.phase_part_2),(self.phase_part_2,self.phase_part_1)]
        for phase_tuple in phases: 
            x = self.find_phase(sorted_hand,phase_tuple[0])
            if not x[0] is None:
                y = self.find_phase(x[0],phase_tuple[1])
                if not y[0] is None:
                    self.hand = y[0]
                    self.phase_part_1 = x[1]
                    self.phase_part_2 = y[1]
                    return True
        return False

    def find_phase(self, hand, pset):
        if pset.complete:
            return hand, pset
        for cardx in hand:
            if pset.can_add(cardx):
                x = self.find_phase([c for c in hand if not c is cardx ], pset.copy_with(cardx))
                if not x[0] is None:
                    return x
        return None, None    



class HumanPlayer(Player):
    def __init__(self):
        super().__init__(0, 0)
    
    def draw_from_discard(self, card):
        print(self)
        print(f"discard = {card}")
        decicion = input("take discard? y/n")
        while not decicion in ["y","n"]:
            decicion = input("take discard? Must answer y/n")
        return decicion == "y"
    
    def evaluate_hand(self):
        print(self)
        choice = -1
        while choice < 0  or choice > len(self.hand)-1:
            try: 
                choice = int(input("Which card should be discarded: (0-10):"))
            except:
                choice = -1
        self.hand[choice].worth = -1
        self.sort_hand()
        self.hand[len(self.hand)-1].worth = 0
            
    
    def __str__(self):
        self.hand.sort(key=lambda card: card.number)
        hand = "---\n"
        for i, card in enumerate(self.hand):
            hand += f"{i}" + ": " + str(card) + "\n"
        return hand

class Phase:
    def __init__(self, phase_number):
        self.phase = phase_number-1
        self.phases = [self.phase1,self.phase2,self.phase3,self.phase4,self.phase5,
                       self.phase6,self.phase7,self.phase8,self.phase9,self.phase10]

    def can_play(self, phand):
        self.phases[self.phase](phand)

    def phase1(self, hand):
        if self.has_set_of(3):
            if self.has_set_of(3):
                return True

    def phase2(self, hand):
        pass

    def phase3(self, hand):
        pass

    def phase4(self, hand):
        pass

    def phase5(self, hand):
        pass

    def phase6(self, hand):
        pass

    def phase7(self, hand):
        pass

    def phase8(self, hand):
        pass

    def phase9(self, hand):
        pass

    def phase10(self, hand):
        pass

class set_of_cards:
    def __init__(self, num_cards):
        """Creates a class that is used to test if a player has the cards to play
        their cards, and also to store the cards once played. This one is for a group
        of cards with the same number value"""
        self.cards = []
        self.number_of_cards = num_cards
        self.number = -1
        self.played = False
        self.complete = False

    def can_add(self, card):
        """checks if a card can be added to this set"""
        if self.number == card.number or self.number == -1:
            return True
        return False
    
    def add_card(self, card):
        """Adds the card to the set and updates the number for the set if it is the first.
        Returns True if set is complete, and False if otherwise"""
        if self.number == -1:
            self.number = card.number
        self.cards.append(card)
        if self.number_of_cards == len(self.cards):
            self.complete = True
        return self.complete
    
    def return_cards(self, hand):
        """Gives the cards currently stored in this set back to the specified hand"""
        for _ in range(len(self.cards)):
            hand.append(self.cards.pop())
        self.number = -1
        self.complete = False
    
    def copy_with(self, cardx):
        copy = set_of_cards(self.number_of_cards)
        for card in self.cards:
            copy.add_card(card)
        copy.add_card(cardx)
        return copy

class run_of_cards:
    def __init__(self, num_cards):
        """Creates a class that is used to test if a player has the cards to play
        their cards, and also to store the cards once played. This one is for a group
        of cards with adjacent number values (similar to a sraight in poker)"""
        self.cards = []
        self.number_of_cards = num_cards
        self.highest_card = -1
        self.lowest_card = -1
        self.played = False

    def can_add(self, card):
        """checks if a card can be added to this run"""
        if (self.lowest_card - 1 == card.number and card.number > 0) or (self.highest_card + 1 == card.number and card.number < 13):
            return True
        return False
    
    def add_card(self, card):
        """Adds the card to the run, and adjusts the highest card and lowest card values.
        Returns True if run is complete, and False if otherwise"""
        if self.highest_card + 1 == card.number or self.highest_card == -1:
            self.highest_card = card.number
        if self.lowest_card - 1 == card.number or self.lowest_card == -1:
            self.lowest_card = card.number
        self.cards.append(card)
        if self.number_of_cards == len(self.cards):
            return True
        else:
            return False
    
    def return_cards(self, hand):

        """Gives the cards currently stored in this run back to the hand"""
        for card in self.cards:
            hand.append(card)
        self.cards = []
        self.highest_card = -1
        self.lowest_card = -1

    def copy_with(self, cardx):
        copy = set_of_cards(self.number_of_cards)
        for card in self.cards:
            copy.add_card(card)
        copy.add_card(cardx)
        return copy

class color_set:
    def __init__(self, num_cards):
        self.cards = []
        self.number_of_cards = num_cards
        self.color = None
