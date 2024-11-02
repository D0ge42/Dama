class AiMoveValidatorClass():
    def __init__(self:object)-> None:
        None

    def can_black_pawn_be_moved(self:object,board,black_pawn_y:int, black_pawn_x:int)-> bool:
        '''
        Check if given black pawn can be moved using coordinates passed to function.
        '''
        #Check that current pawn is in the the middle
        if black_pawn_y == 7:
            return False
        if(black_pawn_x >= 1 and black_pawn_x <= 6 and black_pawn_y <= 6):
            #Check bottom left spot
            if((board[black_pawn_y + 1][black_pawn_x - 1] == "⚪") or (board[black_pawn_y + 1][black_pawn_x - 1] == "⚫")):
                #Check bottom right spot
                if((board[black_pawn_y +1][black_pawn_x + 1] == "⚪") or (board[black_pawn_y +1][black_pawn_x + 1] == "⚫")):
                    return False
        elif(black_pawn_x == 0 or black_pawn_x == 7 and black_pawn_y <= 6):
            #Check if pawn at most left spot has bottom right spot taken
            if((black_pawn_x == 0 and board[black_pawn_y + 1][black_pawn_x + 1] == "⚪") or \
                (black_pawn_x == 0 and board[black_pawn_y + 1][black_pawn_x + 1] == "⚫")):
                return False
            #Check if pawn at most left spot has bottom right spot taken
            elif((black_pawn_x == 7 and board[black_pawn_y + 1][black_pawn_x -1] == "⚪") or \
                (black_pawn_x == 7 and board[black_pawn_y + 1][black_pawn_x - 1] == "⚫")):
                return False
        return True
    
