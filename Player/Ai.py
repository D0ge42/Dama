from Player.Player import PlayerClass
from MoveValidator.MoveValidator import MoveValidatorClass
import random

class AiClass(PlayerClass):
    def __init__(self:object)-> None:
        self.MoveValidator = MoveValidatorClass()        


    def Move(self:object, board:list) -> None:
        '''Function that will automate ai pawn movement'''
        self.board = board
        i = 0
        for rows in self.board:
            for pawn in rows:
                if pawn == "⚫":
                    pawn = " "
                    return
  
        # rand_x = random.randint(0,7)
        # rand_y = random.randint(0,7)
        # if self.board[rand_y][rand_x] != "⚫":
        #     self.board[rand_y][rand_x] = "⚫"
        # else:
        #     rand_x = random.randint(0,7)
        #     rand_y = random.randint(0,7)