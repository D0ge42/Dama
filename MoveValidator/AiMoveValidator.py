import random

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
        if((black_pawn_x >= 1 and black_pawn_x <= 6) and black_pawn_y <= 6):
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
    
    def Available_pawn_moves(self:object,board:list, pawn_color:str, move_y:int, move_x:int)-> None:

        '''Function that after picking a random pawn from the list of pawns
            that can move, will analyze possible moves and pick one randomly.'''

        #                            HANDLE BLACK PAWN POSSIBLE MOVES                            #
        #----------------------------------------------------------------------------------------#

        #Handle black pawns possible moves.
        if pawn_color == "⚫":
            #Remove pawn from current spot. 
            board[move_y][move_x] = "  "
            #We first check most left/right pawns. These pawns can only move left or right
            #We don't need to check if their only move possible has a busy spot because
            #we retrieve pawns from the available black pawns ready to move.
            if (move_x == 0 or move_x == 7 and move_y <= 6):
                if move_x == 0:
                    board[move_y + 1][move_x + 1] = "⚫"
                    print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x +1]}")
                elif move_x == 7:
                    board[move_y + 1][move_x - 1] = "⚫"
                    print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x -1]}")
            #For middle pawns we need to check if either right/left or both spots are available.
            elif (move_x >= 1 and move_x <= 6 and move_y <= 6):
                #If right spot is taken, we move left
                if board[move_y + 1][move_x + 1] == "⚫" or board[move_y + 1][move_x + 1] == "⚪":
                    board[move_y + 1][move_x -1] = "⚫"
                    print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x -1]}")
                #If left spot is taken, we move right
                elif board[move_y + 1][move_x - 1] == "⚫" or board[move_y + 1][move_x - 1] == "⚪":
                    board[move_y + 1][move_x + 1] = "⚫"
                    print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x +1]}")
                #else it means that both spot are available, so we pick one randomly.
                else:
                    lor = (-1,+1)
                    random_move = random.choice(lor)
                    board[move_y + 1][move_x + (random_move)] = "⚫"
                    print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x + random_move]}")
        
        
        #                            HANDLE WHITE PAWN POSSIBLE MOVES                            #
        #----------------------------------------------------------------------------------------#

        #Handle white pawns possible moves.           
        elif pawn_color == "⚪":
            #Remove pawn from current spot. 
            board[move_y][move_x] = "  "
            #We first check most left/right pawns. These pawns can only move left or right
            #We don't need to check if their only move possible has a busy spot because
            #we retrieve pawns from the available black pawns ready to move.
            if (move_x == 0 or move_x == 7) and move_y >= 1:
                if move_x == 0:
                    board[move_y - 1][move_x + 1] = "⚪"
                    print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y -1, move_x + 1]}")
                elif move_x == 7:
                    board[move_y - 1][move_x - 1] = "⚪"
                    print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y -1, move_x -1]}")
            #For middle pawns we need to check if either right/left or both spots are available.
            elif (move_x >= 1 and move_x <= 6 and move_y >= 1):
                #If right spot is taken, we move left
                if board[move_y - 1][move_x + 1] == "⚫" or board[move_y - 1][move_x + 1] == "⚪":
                    board[move_y -1][move_x -1] = "⚪"
                    print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y - 1, move_x -1]}")
                #If left spot is taken, we move right
                elif board[move_y - 1][move_x - 1] == "⚫" or board[move_y - 1][move_x - 1] == "⚪":
                    board[move_y - 1][move_x + 1] = "⚪"
                    print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y -1, move_x +1]}")
                #else it means that both spot are available, so we pick one randomly.
                else:
                    lor = (-1,+1)
                    random_move = random.choice(lor)
                    board[move_y - 1][move_x + (random_move)] = "⚪"
                    print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y - 1, move_x + random_move]}")

    def can_white_pawn_be_moved(self:object,board, white_pawn_y:int, white_pawn_x:int)-> bool:
        '''Function to check whether it is possible to make  any possible move with a white pawn. If not we'll ask user to select another pawn'''
        if white_pawn_y == 0:
            return False
        if((white_pawn_x >= 1 and white_pawn_x <= 6) and (white_pawn_y >= 1)):
            #Check top left spot for middle pawns
            if (board[white_pawn_y - 1][white_pawn_x - 1] == "⚪" or board[white_pawn_y - 1][white_pawn_x - 1] == "⚫"):
                #Check top right spot for middle pawns
                if(board[white_pawn_y -1][white_pawn_x +1] == "⚪" or board[white_pawn_y -1][white_pawn_x + 1] == "⚫"):
                    return False
        elif((white_pawn_x == 0 or white_pawn_x == 7) and (white_pawn_y >= 1)):
            #Check if pawn at most left spot has top right spot taken
            if ((white_pawn_x == 0 and board[white_pawn_y - 1][white_pawn_x +1] == "⚪") or \
                 (white_pawn_x == 0 and board[white_pawn_y - 1][white_pawn_x + 1] == "⚫")):
                return False
            #Check if pawn at most right spot has top left spot taken
            elif ((white_pawn_x == 7 and board[white_pawn_y - 1 ][white_pawn_x - 1] == "⚪") or \
                   (white_pawn_x == 7 and board[white_pawn_y -1][white_pawn_x - 1] == "⚫")):
                return False
        return True
    
    def can_black_pawn_eat(self:object,pawn_color:str, board:list, pawn_y:int, pawn_x:int)-> bool:
        #Check if middle pawn can eat
        if pawn_color == "⚫":
            #Check if most left black pawn can eat
            if ((pawn_x == 0 or pawn_x == 1) and pawn_y <= 5):
                if board[pawn_y + 1][pawn_x + 1] == "⚪" and board[pawn_y + 2][pawn_x + 2] == "  ": ##BUG
                    return True
                else:
                    return False #Can't eat
            #Check if middle black pawn can eat
            elif ((pawn_x >= 2 and pawn_x <= 5) and pawn_y <= 5):
                if board[pawn_y + 1][pawn_x + 1] == "⚪" and board[pawn_y + 2][pawn_x + 2] == "  " or \
                    board[pawn_y + 1][pawn_x - 1] == "⚪" and board[pawn_y + 2][pawn_x - 2] == "  ":
                    return True
                else:
                    return False #Can't eat
            #Check if most right black pawn can eat
            elif ((pawn_x == 7 or pawn_x == 6) and pawn_y <= 5):
                if board[pawn_y + 1][pawn_x -1] == "⚪" and board[pawn_y + 2][pawn_x - 2] == "  ": ##BUG
                    return True
                else:
                    return False #Can't eat
            else:
                return False
        else:
            return False
        
    def can_white_pawn_eat(self:object,pawn_color:str, board:list, pawn_y:int, pawn_x:int)-> bool:
        #Check if middle pawn can eat
        if pawn_color == "⚪":
            #Check if most left white pawn can eat
            if ((pawn_x == 0 or pawn_x == 1) and pawn_y >= 2):
                if board[pawn_y -1][pawn_x + 1] == "⚫" and board[pawn_y - 2][pawn_x + 2] == "  ":
                    return True
                else:
                    return False
            #Check if middle white pawn can eat
            elif ((pawn_x >= 2 and pawn_x <= 5) and pawn_y <= 5):
                if board[pawn_y - 1][pawn_x + 1] == "⚫" and board[pawn_y - 2][pawn_x + 2] == "  " or \
                    board[pawn_y - 1][pawn_x - 1] == "⚫" and board[pawn_y - 2][pawn_x - 2] == "  ":
                    return True
                else:
                    return False
            #Check if most right white pawn can eat
            elif ((pawn_x == 7 or pawn_x == 6) and pawn_y >= 2):
                if board[pawn_y - 1][pawn_x - 1] == "⚫" and board[pawn_y - 2][pawn_x - 2] == "  ":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False 
