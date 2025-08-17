from Card_and_Deck import Card, Deck
from Players_and_Strats import Player, HumanPlayer

bernard = Player(0,0)

bernard.hand = [Card("blue", (i % 5) + 1) for i in range(1,12)]

if bernard.can_play_down():
    print("YIPEEEEEEEEEEEE")
else:
    print("damit")
