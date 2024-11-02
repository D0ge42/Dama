import random

class AiUtility():
    def __init__(self:object)-> None:
        pass

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
