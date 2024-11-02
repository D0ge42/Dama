from Player.Player import PlayerClass
from MoveValidator.AiMoveValidator import AiMoveValidatorClass
from MoveValidator.PlayerMoveValidator import PlayerMoveValidatorClass
from Ai_utility.Ai_Utility import AiUtility
import random

class AiClass(PlayerClass):
    def __init__(self:object)-> None:
        self.AiMoveValidator = AiMoveValidatorClass()
        self.AiUtility = AiUtility()
        self.PlayerMoveValidator = PlayerMoveValidatorClass()


    def Available_black_pawn(self:object, board:list) -> list:
        '''Function that will check available black pawns'''
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
    
    def Available_white_pawn(self:object, board:list) -> list:
        '''Function that will check available white pawns'''
        self.white_pawns = 0
        self.board = board
        self.possible_white_pawns = []
        #Iterate list of pawn.
        for rows_index, row in enumerate(self.board):
            for col_index, pawn in enumerate(row):
                #Extrapolate black pawns
                if pawn == "⚪":
                    self.white_pawns += 1
                    #Check if extrapolated black pawns can move in any direction.
                    if self.PlayerMoveValidator.can_white_pawn_be_moved(self.board, rows_index, col_index):
                           #Make a list of possible movable black pawns.
                           self.possible_white_pawns.append(str(rows_index) + str(col_index))
        print(f"Pedine bianche = {self.white_pawns}")
        return self.possible_white_pawns
    
    def Move(self:object,board:list, turn:str)-> None:
        '''Function that will use list of possible moves to make random moves.
           We'll use this function to let 2 bot play against eachothers.'''
        
        if turn == "Black":
            print(f"Mosse nere disponibili: {len(self.possible_moves)}")
            if len(self.possible_moves) >= 1:
                self.move_to_do_black = random.choice(self.possible_moves)
                if board[int(self.move_to_do_black[0])][int(self.move_to_do_black[1])] == "⚫":
                    self.AiUtility.Available_pawn_moves(self.board,"⚫",int(self.move_to_do_black[0]), int(self.move_to_do_black[1]))

        elif turn == "White":
            print(f"Mosse bianche disponibili: {len(self.possible_white_pawns)}")
            if len(self.possible_white_pawns) >= 1:
                self.move_to_do_white = random.choice(self.possible_white_pawns)
                if board[int(self.move_to_do_white[0])][int(self.move_to_do_white[1])] == "⚪":
                        self.AiUtility.Available_pawn_moves(self.board,"⚪",int(self.move_to_do_white[0]), int(self.move_to_do_white[1]))

    # def Eat(self:object, board:list, pawn_color:str):
    #     #eat right or left
    #     if pawn_color == "⚪":
    #         print(f"Y: {int(self.move_to_do_white[0])}, X: {int(self.move_to_do_white[1])}")
    #         #check if pawn can eat top right
    #         if self.move_to_do_white[0] + 2 >= 7 and self.move_to_do_white[0] +2 >= 7:
    #             if board[self.move_to_do_white[0] - 1][self.move_to_do_white[1] + 1] == "⚫" and board[self.move_to_do_white[0] - 2][self.move_to_do_white[1] + 2] == "  ":
    #                 board[self.move_to_do_white[0]][self.move_to_do_white[1]] == "  "
    #                 board[self.move_to_do_white[0] -1][self.move_to_do_white[1] +1] == "  "
    #                 board[self.move_to_do_white[0] - 2][self.move_to_do_white[0] + 2] = "⚪"
    #                 print(f"Pedina bianca {[self.move_to_do_white[0],self.move_to_do_white[1]]} ha mangiato Pedina nera {[self.move_to_do_white[0] -1, self.move_to_do_white[0] + 1]}")
    #             else:
    #                 pass
    #     else:
    #         pass