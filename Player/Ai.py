from Player.Player import PlayerClass
from MoveValidator.AiMoveValidator import AiMoveValidatorClass
import random

class AiClass(PlayerClass):
    def __init__(self:object)-> None:
        self.AiMoveValidator = AiMoveValidatorClass()        


    def Available_black_pawn_moves(self:object, board:list) -> list:
        '''Function that will automate ai pawn movement'''
        self.board = board
        self.possible_moves = []
        #Iterate list of pawn.
        for rows_index, row in enumerate(self.board):
            for col_index, pawn in enumerate(row):
                #Extrapolate black pawns
                if pawn == "⚫":
                    #Check if extrapolated black pawns can move in any direction.
                    if self.AiMoveValidator.can_black_pawn_be_moved(self.board, rows_index, col_index):
                           #Make a list of possible movable black pawns.
                           self.possible_moves.append(str(rows_index) + str(col_index))
        return self.possible_moves
    
    def Move(self:object,board:list, possible_moves:list)-> None:
        possible_moves = self.possible_moves
        move_to_do = random.choice(possible_moves)
        board[int(move_to_do[0])][int(move_to_do[1])] = "  "
        board[int(move_to_do[0]) + 1][int(move_to_do[1]) + 1] = "⚫"
        print(move_to_do)