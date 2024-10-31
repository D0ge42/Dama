
class GeneralMoveValidatorClass():
    def __init__(self:object):
        None
    
    #-----------------------------------------------------------------#
    #                  GENERAL MOVE VALIDATORS                        #
    #-----------------------------------------------------------------#

    def is_pawn_in_range(self:object, pawn_y:int, pawn_x:int)-> bool:
        '''Check whether the pawn coordinates are in range'''
        if (pawn_x >= 0 and pawn_x <= 7) and (pawn_y >= 0 and pawn_y <= 7):
            return True
        else:
            return False
        
    def is_spot_taken(self:object, board:list, move_y:int, move_x:int):
        '''Function to check whether the spot is taken or not by another black or white pawn'''
        if board[move_y][move_x] == "⚫" or board[move_y][move_x] == "⚪":
            return True
        else:
            return False
        
    def is_move_in_range(self:object, move_y:int, move_x:int)-> bool:
        '''Function to check whether the user input move is out of the board or not'''
        if (move_y >= 0 and move_y <= 7) and (move_x >= 0 and move_x <= 7):
            return True
        else:
            return False