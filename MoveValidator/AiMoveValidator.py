import random
from DamaPawn.Damapawn import DamaPawnClass

class AiMoveValidatorClass():
    def __init__(self:object)-> None:
        self.DamaPawn = DamaPawnClass

    def can_black_pawn_be_moved(self:object,board,black_pawn_y:int, black_pawn_x:int)-> bool:
        '''
        Check if given black pawn can be moved using coordinates passed to function.
        '''
        #Check that current pawn is in the the middle
        if black_pawn_y == 7:
            return False
        if((black_pawn_x >= 1 and black_pawn_x <= 6) and black_pawn_y <= 6):
            #Check bottom left spot
            if((board[black_pawn_y + 1][black_pawn_x - 1] == "⚪") or (board[black_pawn_y + 1][black_pawn_x - 1] == "⚫") \
               or (board[black_pawn_y + 1][black_pawn_x - 1] == "🤍") or (board[black_pawn_y + 1][black_pawn_x - 1] == "🖤")):
                #Check bottom right spot
                if((board[black_pawn_y +1][black_pawn_x + 1] == "⚪") or (board[black_pawn_y +1][black_pawn_x + 1] == "⚫")\
               or (board[black_pawn_y + 1][black_pawn_x + 1] == "🤍") or (board[black_pawn_y + 1][black_pawn_x + 1] == "🖤")):
                    return False
        elif(black_pawn_x == 0 or black_pawn_x == 7 and black_pawn_y <= 6):
            #Check if pawn at most left spot has bottom right spot taken
            if((black_pawn_x == 0 and board[black_pawn_y + 1][black_pawn_x + 1] == "⚪") or \
                (black_pawn_x == 0 and board[black_pawn_y + 1][black_pawn_x + 1] == "⚫") or \
                  (black_pawn_x == 0 and board[black_pawn_y + 1][black_pawn_x + 1] == "🖤")or \
                    (black_pawn_x == 0 and board[black_pawn_y + 1][black_pawn_x + 1] == "🤍")) :
                return False
            #Check if pawn at most right spot has bottom left spot taken
            elif((black_pawn_x == 7 and board[black_pawn_y + 1][black_pawn_x -1] == "⚪")or \
                 (black_pawn_x == 7 and board[black_pawn_y + 1][black_pawn_x - 1] == "⚫")or \
                  (black_pawn_x == 0 and board[black_pawn_y + 1][black_pawn_x - 1] == "🖤")or \
                    (black_pawn_x == 0 and board[black_pawn_y + 1][black_pawn_x - 1] == "🤍")) :
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
                if board[move_y + 1][move_x + 1] == "⚫" or board[move_y + 1][move_x + 1] == "⚪" or \
                    board[move_y + 1][move_x + 1] == "🖤" or board[move_y + 1][move_x + 1] == "🤍":
                    board[move_y + 1][move_x -1] = "⚫"
                    print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x -1]}")
                #If left spot is taken, we move right
                elif board[move_y + 1][move_x - 1] == "⚫" or board[move_y + 1][move_x - 1] == "⚪" or \
                     board[move_y + 1][move_x - 1] == "🖤" or board[move_y + 1][move_x - 1] == "🤍":
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
                if board[move_y - 1][move_x + 1] == "⚫" or board[move_y - 1][move_x + 1] == "⚪"or \
                    board[move_y - 1][move_x + 1] == "🖤" or board[move_y - 1][move_x + 1] == "🤍":
                    board[move_y -1][move_x -1] = "⚪"
                    print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y - 1, move_x -1]}")

                #If left spot is taken, we move right
                elif board[move_y - 1][move_x - 1] == "⚫" or board[move_y - 1][move_x - 1] == "⚪"or \
                    board[move_y - 1][move_x - 1] == "🖤" or board[move_y - 1][move_x - 1] == "🤍":
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
            if (board[white_pawn_y - 1][white_pawn_x - 1] == "⚪" or board[white_pawn_y - 1][white_pawn_x - 1] == "⚫")or \
                (board[white_pawn_y - 1][white_pawn_x - 1] == "🤍" or board[white_pawn_y - 1][white_pawn_x - 1] == "🖤"):
                #Check top right spot for middle pawns
                if(board[white_pawn_y -1][white_pawn_x +1] == "⚪" or board[white_pawn_y -1][white_pawn_x + 1] == "⚫") or \
                    (board[white_pawn_y -1][white_pawn_x +1] == "🤍" or board[white_pawn_y -1][white_pawn_x + 1] == "🖤"):
                    return False
        elif((white_pawn_x == 0 or white_pawn_x == 7) and (white_pawn_y >= 1)):
            #Check if pawn at most left spot has top right spot taken
            if ((white_pawn_x == 0 and board[white_pawn_y - 1][white_pawn_x +1] == "⚪") or \
                 (white_pawn_x == 0 and board[white_pawn_y - 1][white_pawn_x + 1] == "⚫"))or\
                    (white_pawn_x == 0 and board[white_pawn_y - 1][white_pawn_x +1] == "🤍")or\
                        (white_pawn_x == 0 and board[white_pawn_y - 1][white_pawn_x +1] == "🖤"):
                return False
            #Check if pawn at most right spot has top left spot taken
            elif ((white_pawn_x == 7 and board[white_pawn_y - 1 ][white_pawn_x - 1] == "⚪")or \
                    (white_pawn_x == 7 and board[white_pawn_y -1][white_pawn_x - 1] == "⚫")or\
                    (white_pawn_x == 7 and board[white_pawn_y -1][white_pawn_x - 1] == "🤍")or\
                    (white_pawn_x == 7 and board[white_pawn_y -1][white_pawn_x - 1] == "🖤")):
                return False
        return True
    
    def can_black_pawn_eat(self:object,pawn_color:str, board:list, pawn_y:int, pawn_x:int)-> bool:
        #Check if middle pawn can eat
        if pawn_color == "⚫":
            #Check if most left black pawn can eat
            if ((pawn_x == 0 or pawn_x == 1) and pawn_y <= 5):
                if board[pawn_y + 1][pawn_x + 1] == "⚪" and board[pawn_y + 2][pawn_x + 2] == "  ": 
                    return True
            #Check if middle black pawn can eat
            elif ((pawn_x >= 2 and pawn_x <= 5) and pawn_y <= 5):
                if board[pawn_y + 1][pawn_x + 1] == "⚪" and board[pawn_y + 2][pawn_x + 2] == "  " or \
                    board[pawn_y + 1][pawn_x - 1] == "⚪" and board[pawn_y + 2][pawn_x - 2] == "  ":
                    return True
            #Check if most right black pawn can eat
            elif ((pawn_x == 7 or pawn_x == 6) and pawn_y <= 5):
                if board[pawn_y + 1][pawn_x -1] == "⚪" and board[pawn_y + 2][pawn_x - 2] == "  ":
                    return True
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
                        
    def can_crowned_pawn_move(self:object, board:list, crown_y:int, crown_x:int):
        '''
        This function will give us a list of possible moves we can make
        or False if we can't make any move. This is to make it so we won't need
        2 functions to check if we can move  and where.
        '''
        self.DamaClass = DamaPawnClass()
        moves = []
        if crown_y == 7:
            if crown_x >= 1 and crown_x <= 6:
                moves = []
                if (self.DamaClass.CheckTopLeft(board, crown_y, crown_x)):
                        moves.append(1)
                if (self.DamaClass.CheckTopRight(board, crown_y, crown_x)): 
                        moves.append(2)
            elif crown_x == 0:
                    moves = []
                    if self.DamaClass.CheckTopRight(board, crown_y, crown_x):
                        moves.append(2)
            elif crown_x == 7:
                moves = []
                if self.DamaClass.CheckTopLeft(board, crown_y, crown_x): 
                     moves.append(1)
        elif crown_y == 0:
            moves = []
            if crown_x >= 1 and crown_x <= 6:
                if self.DamaClass.CheckBottomLeft(board, crown_y, crown_x):
                    moves.append(4)
                if self.DamaClass.CheckBottomRight(board, crown_y, crown_x):
                    moves.append(3) 
            elif crown_x == 0:
                moves = []
                if self.DamaClass.CheckBottomRight(board, crown_y, crown_x):
                    moves.append(3)
            elif crown_x == 7:
                moves = []
                if  self.DamaClass.CheckBottomLeft(board, crown_y, crown_x):
                    moves.append(4)
        elif (crown_y >= 1 and crown_y <= 6) and crown_x == 0:
            moves = []
            if  self.DamaClass.CheckTopRight(board, crown_y, crown_x):
                moves.append(2)
            if self.DamaClass.CheckBottomRight(board, crown_y, crown_x):
                moves.append(3)
        elif (crown_y >= 1 and crown_y <= 6) and crown_x == 7:
            moves = []
            if self.DamaClass.CheckTopLeft(board, crown_y, crown_x):
                moves.append(1)
            if self.DamaClass.CheckBottomLeft(board, crown_y, crown_x):
                moves.append(4)
        elif (crown_y >= 1 and crown_y <=6) and (crown_x >= 1 and crown_x <= 6):
            moves = []
            if  self.DamaClass.CheckTopLeft(board, crown_y, crown_x):
                moves.append(1)
            if  self.DamaClass.CheckTopRight(board, crown_y, crown_x):
                moves.append(2)
            if self.DamaClass.CheckBottomRight(board, crown_y, crown_x):
                moves.append(3)
            if self.DamaClass.CheckBottomLeft(board, crown_y, crown_x):
                moves.append(4)
        if len(moves) >= 1:
            return moves
        else:
            return False
                
    def can_crowned_eat(self:object, pawn_color:str, board:list, pawn_y:int, pawn_x:int)-> bool: #✅
        self.DamaPawn = DamaPawnClass()
        eat = []
        if pawn_color == "Black":
            color = "Black"
        elif pawn_color == "White":
            color = "White"
        #Controllo pedine X <= 1 E Y >= 6📌
        #Se x è compreso tra 0 e 1 e y >= 6 -> Queste pedine possono solo mangiare in alto a destra. #✅
        if pawn_y >= 6 and pawn_x <= 1:
            eat = []
            if self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                eat.append(2) 
        #Controllo pedine X >= 6 E Y >= 6📌
        #Se x è maggiore uguale a 6 e y è maggiore uguale a 6 --> Queste pedine possono solo mangiare in alto a sinistra. ✅ -> cambiato <= 6 con >= 6
        elif pawn_x >= 6 and pawn_y >= 6:
            eat = []
            if self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                eat.append(1)
        #Controllo pedine X <= 1 E Y <= 1📌
        #Se x è <= 1 e y <= 1 --> Queste pedine possono solo mangiare in basso a destra. ✅
        elif pawn_x <= 1 and pawn_y <= 1:
            eat = []
            if self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                eat.append(3)
        #Controllo pedine X >= 6 e Y <= 1📌
        #Se x è >= 6 e y <= 1 --> Queste pedine possono solo mangiare in basso a sinistra. ✅
        elif pawn_x >= 6 and pawn_y <= 1:
            eat = []
            if self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                eat.append(4)
        #Controllo pedine X <= 1 E Y >= 2 E Y <= 5📌
        #Se x <= 1 e Y compreso tra 2 e 5 --> Queste pedine possono mangiare sia in basso a destra che in alto a destra. ✅
        elif (pawn_x <= 1) and (pawn_y >= 2 and pawn_y <= 5):
            eat = []
            if self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                eat.append(2)
            if self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                eat.append(3)
        #Controllo pedine X >= 6 E Y >= 2 E Y <= 5📌
        # Se x è maggiore uguale a 6 e Y compreso tra 2 e 5 --> Queste pedine possono sia mangiare in basso che in alto a sinistra. ✅
        elif (pawn_x >= 6 ) and (pawn_y >= 2 and pawn_y <= 5):
            eat = []
            if self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                eat.append(1)
            if self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                eat.append(4)
        #Controllo pedine X compreso tra 2 e 5 e Y maggiore uguale a 6📌
        #Se x è compreso tra 2 e 5 e y maggiore uguale a 6 --> Queste pedine possono solo mangiare in alto a destra o sinistra.✅
        elif (pawn_x >= 2 and pawn_x <= 5) and pawn_y >= 6:
            eat = []
            if self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                eat.append(1)
            if self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                eat.append(2)
        #Controllo pedine X compreso tra 2 e 5 e Y minore uguale a 1📌
        #Se x è compreso tra 2 e 5 e Y minore uguale a 1 --> Queste pedine possono solo mangiare in basso a destra o sinistra ✅
        elif (pawn_x >= 2 and pawn_x <= 5) and pawn_y <= 1:
            eat = []
            if self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                eat.append(3)
            if self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                eat.append(4)
        #Controllo pedine X compreso tra 2 e 5 e Y compreso tra 2 e 5.📌
        #Se X è compreso tra 2 e 5 e Y è compreso tra 2 e 5 --> Queste pedine possono mangiare in ogni direzione.
        elif (pawn_x >= 2 and pawn_x <= 5) and (pawn_y >= 2 and pawn_y <= 5):
            eat = []
            if self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                eat.append(1)
            if self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                eat.append(2)
            if self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                eat.append(3)   
            if self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                eat.append(4)
        
        if len(eat) >= 1:
            return eat
        else:
            return False 
                
            


