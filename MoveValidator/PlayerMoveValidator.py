
class PlayerMoveValidatorClass():
    def __init__(self:object):
        None
     
    #-------------------------------------------------------------------#
    #                     WHITE PLAYER VALIDATORS                       #
    # ------------------------------------------------------------------#        

    def is_pawn_white(self:object, white_pawn:str):
        '''Method to check whether the selected pawn is white or existent'''
        if white_pawn != "⚪":
            return False
        else:
            return True

    def can_white_pawn_be_moved(self:object,board, white_pawn_y:int, white_pawn_x:int)-> bool:
        '''Function to check whether it is possible to make  any possible move with a white pawn. If not we'll ask user to select another pawn'''
     
        if(white_pawn_x >= 1 and white_pawn_x <= 6):
            #Check top left spot for middle pawns
            if (board[white_pawn_y - 1][white_pawn_x - 1] == "⚪" or board[white_pawn_y - 1][white_pawn_x - 1] == "⚫"):
                #Check top right spot for middle pawns
                if(board[white_pawn_y -1][white_pawn_x +1] == "⚪" or board[white_pawn_y -1][white_pawn_x + 1] == "⚫"):
                    return False
        elif(white_pawn_x == 0 or white_pawn_x == 7):
            #Check if pawn at most left spot has top right spot taken
            if ((white_pawn_x == 0 and board[white_pawn_y - 1][white_pawn_x +1] == "⚪") or \
                 (white_pawn_x == 0 and board[white_pawn_y - 1][white_pawn_x + 1] == "⚫")):
                return False
            #Check if pawn at most right spot has top left spot taken
            elif ((white_pawn_x == 7 and board[white_pawn_y - 1 ][white_pawn_x - 1] == "⚪") or \
                   (white_pawn_x == 7 and board[white_pawn_y -1][white_pawn_x - 1] == "⚫")):
                return False
        return True
     

    def validate_white_move(self:object, white_pawn:int, white_move:int) -> bool:
        '''Method that will check if the move is diagonal by subtraction.
            Valid moves in dama will either have a difference of 9 or 11 for white pawns'''
        
        if (white_pawn - white_move == 9) or (white_pawn - white_move == 11):
            return True
        else:
            return False
    