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

        # ph
        self.points = 0
        self.phase = 1

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

    def draw_from_discard(self, card):
        """evaluates discard pile card (in context of hand) and draw pile card (based on known cards)
        and outputs false (draw pile) or true (discard pile) to draw from"""
        pass

    def evaluate_hand(self):
        """takes in the hand and information from game manager, checks if play is possible, 
        then orders hand with last card as the one to discard"""
        pass

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
        self.cards = []
        self.number_of_cards = num_cards
        self.number = 0
    

class run_of_cards:
    def __init__(self, num_cards):
        self.cards = []
        self.number_of_cards = num_cards
        self.lowest_card = 0
        self.highest_card = 0

class color_set:
    def __init__(self, num_cards):
        self.cards = []
        self.number_of_cards = num_cards
        self.color = None
        