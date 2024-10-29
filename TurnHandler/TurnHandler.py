import random

class turnHandler():
    def __init__(self:object) -> None:
        self.random = ("White", "Black")


    def randomTurn(self:object) -> str:
        random_turn = random.choice(self.random)
        if random_turn == "White":
            print("Inizia White")
            return "White"
        else:
            print("Inizia Black")
            return "Black"
