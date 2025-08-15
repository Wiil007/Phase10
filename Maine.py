from Card_and_Deck import Card, Deck
from Players_and_Strats import Player, HumanPlayer
from Game_Manager import GameManager

employees = [HumanPlayer(), HumanPlayer()]

corprate = GameManager(employees)
print("starting game")
while True:
    corprate.tick()
    if input("Stop? y/n") == "y":
        break
    