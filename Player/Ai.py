from Player.Player import PlayerClass
from MoveValidator.AiMoveValidator import AiMoveValidatorClass
from DamaPawn.Damapawn import DamaPawnClass
import random

class AiClass(PlayerClass):
    def __init__(self:object)-> None:
        self.AiMoveValidator = AiMoveValidatorClass()
        self.DamaPawn = DamaPawnClass()


    def Available_black_pawn(self:object, board:list) -> list:
        """Function that will check for possible availables black pawns

        Args:
            self (object):
            board (list): [2D list that represents board]

        Returns:
            list: [list of lists, containing 2 lists. 
                  First one will be filled with black pawns that can move
                  Second one will be filled with black pawns that can eat]
        """
        self.board = board
        self.possible_movable_black_pawns = []
        self.possible_black_pawns_that_can_eat = []
        #Iterate list of pawn.
        for rows_index, row in enumerate(self.board):
            for col_index, pawn in enumerate(row):
                #Extrapolate black pawns
                if pawn == "⚫":
                    #Check if extrapolated black pawns can move in any direction.
                    if self.AiMoveValidator.can_black_pawn_be_moved(self.board, rows_index, col_index):
                        #Make a list of possible movable black pawns.
                        self.possible_movable_black_pawns.append(str(rows_index) + str(col_index))
                    if self.AiMoveValidator.can_black_pawn_eat("⚫",self.board,int(rows_index),int(col_index)) == True:
                        #Make a list of possible black pawn that can Eat a white pawn.
                        self.possible_black_pawns_that_can_eat.append(str(rows_index) + str(col_index))
        return [self.possible_movable_black_pawns,self.possible_black_pawns_that_can_eat]

    def Available_crowned_pawns(self:object, board:list, turn:str)-> list:
        """Function that will check for available crowned pawns.

        Args:
            self (object):
            board (list): [2d list representing board]
            turn (str): [turn will be a string (emoji) reprensting either black or white turn]

        Returns:
            list: [list of 2 lists. 
                    First will be movable crowned pans.
                    Second will be crowned pawns that can eat]
        """
        self.board = board
        self.possible_movable_crowned_black_pawns = []
        self.possible_movable_crowned_white_pawns = []
        self.possible_crowned_black_pawns_that_can_eat = []
        self.possible_crowned_white_pawns_that_can_eat = []
        for rows_index, row in enumerate(self.board):
            for col_index, pawn in enumerate(row):
                #Extrapolate black crowned pawns
                    if pawn == "🖤":
                        #List of available crowned pawns that can eat
                        if self.AiMoveValidator.can_crowned_eat("Black",self.board,int(rows_index), int(col_index)):
                            self.possible_crowned_black_pawns_that_can_eat.append(str(rows_index) + str(col_index))
                        #List of available crowned pawns that can move
                        if self.AiMoveValidator.can_crowned_pawn_move(self.board,int(rows_index),int(col_index)):
                            #Make a list of possible black pawn that can Eat a white pawn.
                            self.possible_movable_crowned_black_pawns.append(str(rows_index) + str(col_index))
                    elif pawn == "🤍":
                        if self.AiMoveValidator.can_crowned_eat("White",self.board,int(rows_index), int(col_index)):
                            self.possible_crowned_white_pawns_that_can_eat.append(str(rows_index) + str(col_index))
                        if self.AiMoveValidator.can_crowned_pawn_move(self.board,int(rows_index),int(col_index)):
                            #Make a list of possible black pawn that can Eat a white pawn.
                            self.possible_movable_crowned_white_pawns.append(str(rows_index) + str(col_index))
        if turn == "Black":
            return [self.possible_movable_crowned_black_pawns,self.possible_crowned_black_pawns_that_can_eat]
        elif turn == "White":
            return [self.possible_movable_crowned_white_pawns,self.possible_crowned_white_pawns_that_can_eat]

    def Available_white_pawn(self:object, board:list) -> list:
        '''Function that will check available white pawns'''
        self.board = board
        self.possible_movable_white_pawns = []
        self.possible_white_pawns_that_can_eat = []
        #Iterate list of pawn.
        for rows_index, row in enumerate(self.board):
            for col_index, pawn in enumerate(row):
                #Extrapolate black pawns
                if pawn == "⚪": 
                    #Check if extrapolated black pawns can move in any direction.
                    if self.AiMoveValidator.can_white_pawn_be_moved(self.board, rows_index, col_index):
                        #Make a list of possible movable black pawns.
                        self.possible_movable_white_pawns.append(str(rows_index) + str(col_index))
                    if self.AiMoveValidator.can_white_pawn_eat("⚪",self.board,rows_index,col_index):
                        #Make a list of possible white paw that can eat
                        self.possible_white_pawns_that_can_eat.append(str(rows_index) + str(col_index))
        return [self.possible_movable_white_pawns, self.possible_white_pawns_that_can_eat]
    
    def Move(self:object,board:list, turn:str)-> None:
        '''Function that will use list of possible moves to make random moves.
           We'll use this function to let 2 bot play against eachothers.'''
        
        if turn == "Black":
            if len(self.possible_movable_black_pawns) >= 1:
                self.move_to_do_black = random.choice(self.possible_movable_black_pawns)
                move_y  = int(self.move_to_do_black[0])
                move_x = int(self.move_to_do_black[1])
                #self.AiMoveValidator.available_pawn_moves(self.board,"⚫",int(self.move_to_do_black[0]), int(self.move_to_do_black[1]))
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
                    if not self.DamaPawn.CheckBottomRight(board, move_y, move_x):
                        board[move_y + 1][move_x -1] = "⚫"
                        print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x -1]}")
                    #If left spot is taken, we move right
                    elif not self.DamaPawn.CheckBottomLeft(board, move_y, move_x):
                        board[move_y + 1][move_x + 1] = "⚫"
                        print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x +1]}")
                    #else it means that both spot are available, so we pick one randomly.
                    else:
                        random_move = random.choice((-1,+1))
                        board[move_y + 1][move_x + (random_move)] = "⚫"
                        print(f"Ai moves black pawn from {[move_y,move_x]} to {[move_y+1, move_x + random_move]}")

        elif turn == "White":
            if len(self.possible_movable_white_pawns) >= 1:
                self.move_to_do_white = random.choice(self.possible_movable_white_pawns)
                move_y = int(self.move_to_do_white[0])
                move_x = int(self.move_to_do_white[1])
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
                    if  not self.DamaPawn.CheckTopRight(board, move_y, move_x): 
                        board[move_y -1][move_x -1] = "⚪"
                        print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y - 1, move_x -1]}")
                    #If left spot is taken, we move right
                    elif not self.DamaPawn.CheckTopLeft(board, move_y, move_x):
                        board[move_y - 1][move_x + 1] = "⚪"
                        print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y -1, move_x +1]}")
                    #else it means that both spot are available, so we pick one randomly.
                    else:
                        random_move = random.choice((-1,+1))
                        board[move_y - 1][move_x + (random_move)] = "⚪"
                        print(f"Ai moves white pawn from {[move_y,move_x]} to {[move_y - 1, move_x + random_move]}")
    
    def Eat(self:object, board:list, turn:str)-> None: #Implement possibility to eat crowned pawns
        '''
        Function that will use lists of possible  pawns that can eat to perform an "Eat" Action.
        '''
        #                                                                                               #
        #                               IF IT'S BLACK TURN                                              #
        #-----------------------------------------------------------------------------------------------#
        if turn == "Black":
            if len(self.possible_black_pawns_that_can_eat):
                random_black_pawn_eat = random.choice(self.possible_black_pawns_that_can_eat)
            else:
                return False
            pawn_y = int(random_black_pawn_eat[0]) #Get Y coordinates of selected pawn that can Eat
            pawn_x = int(random_black_pawn_eat[1]) #Get X coordinates of selected pawn that can Eat
                #Check if most left black pawn can eat
            if ((pawn_x == 0 or pawn_x == 1) and pawn_y <= 5):
                #If this is true then it means we can do an Eat action.
                if board[pawn_y + 1][pawn_x + 1] == "⚪" and board[pawn_y + 2][pawn_x + 2] == "  ":
                    board[pawn_y][pawn_x] = "  "
                    board[pawn_y + 1][pawn_x + 1] = "  "
                    board[pawn_y + 2][pawn_x + 2] = "⚫"
                    print(f"Black pawn {pawn_y}{pawn_x} eat White Pawn {pawn_y+1}{pawn_x+1} and ends up at {pawn_y +2}{pawn_x + 2}") #✅ Checked
                else:
                    return False #Can't eat
            #Check if middle black pawn can eat
            elif ((pawn_x >= 2 and pawn_x <= 5) and pawn_y <= 5):

                if (board[pawn_y + 1][pawn_x + 1] == "⚪" and board[pawn_y + 2][pawn_x + 2] == "  ") or \
                (board[pawn_y + 1][pawn_x - 1] == "⚪" and board[pawn_y + 2][pawn_x - 2] == "  "):
                    random_num_b = random.choice((0,1))
                    #If random num is 0 we eat bottom left if its possible
                    #else we eat bottom right
                    if random_num_b == 0:
                        if(board[pawn_y + 1][pawn_x - 1] == "⚪" and board[pawn_y + 2][pawn_x - 2] == "  "):
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y + 1][pawn_x - 1] = "  "
                            board[pawn_y + 2][pawn_x - 2] = "⚫"
                            print(f"Black pawn {pawn_y}{pawn_x} eat White Pawn {pawn_y+1}{pawn_x - 1} and ends up at {pawn_y +2}{pawn_x - 2}") #✅ Checked

                        elif (board[pawn_y + 1][pawn_x + 1] == "⚪" and board[pawn_y + 2][pawn_x + 2] == "  "):
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y + 1][pawn_x + 1] = "  "
                            board[pawn_y + 2][pawn_x + 2] = "⚫"
                            print(f"Black pawn {pawn_y}{pawn_x} eat White Pawn {pawn_y+1}{pawn_x+1} and ends up at {pawn_y +2}{pawn_x + 2}") #✅ Checked

                    #If random num is 1 we eat bottom right if its possible
                    #else we eat bottom left
                    elif random_num_b == 1:
                        if(board[pawn_y + 1][pawn_x + 1] == "⚪" and board[pawn_y + 2][pawn_x + 2] == "  "):
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y + 1][pawn_x + 1] = "  "
                            board[pawn_y + 2][pawn_x + 2] = "⚫"
                            print(f"Black pawn {pawn_y}{pawn_x} eat White Pawn {pawn_y+1}{pawn_x+1} and ends up at {pawn_y +2}{pawn_x + 2}")

                        elif (board[pawn_y + 1][pawn_x - 1] == "⚪" and board[pawn_y + 2][pawn_x - 2] == "  "):
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y + 1][pawn_x - 1] = "  "
                            board[pawn_y + 2][pawn_x - 2] = "⚫"
                            print(f"Black pawn {pawn_y}{pawn_x} eat White Pawn {pawn_y+1}{pawn_x-1} and ends up at {pawn_y +2}{pawn_x - 2}") #✅ Checked
                else:
                    return False #Can't eat
                
            #Check if most right black pawn can eat
            elif ((pawn_x == 7 or pawn_x == 6) and pawn_y <= 5):
                 #If this is true then it means we can do an Eat action.
                if board[pawn_y + 1][pawn_x -1] == "⚪" and board[pawn_y + 2][pawn_x - 2] == "  ":
                    board[pawn_y][pawn_x] = "  "
                    board[pawn_y + 1][pawn_x - 1] = "  "
                    board[pawn_y + 2][pawn_x - 2] = "⚫"
                    print(f"Black pawn {pawn_y}{pawn_x} eat White Pawn {pawn_y+1}{pawn_x -1} and ends up at {pawn_y +2}{pawn_x - 2}") #✅ Checked
                else:
                    return False #Can't eat
            else:
                return False
        #                                                                                               #
        #                               IF IT'S WHITE TURN                                              #
        #-----------------------------------------------------------------------------------------------#
        elif turn == "White":
            if len(self.possible_white_pawns_that_can_eat):
                random_white_pawn_eat = random.choice(self.possible_white_pawns_that_can_eat)
            else:
                return False
            pawn_y = int(random_white_pawn_eat[0]) #Get Y coordinates of selected pawn that can Eat
            pawn_x = int(random_white_pawn_eat[1]) #Get X coordinates of selected pawn that can Eat
            #Check if most left white pawn can eat
            if ((pawn_x == 0 or pawn_x == 1) and pawn_y >= 2):
                if board[pawn_y -1][pawn_x + 1] == "⚫" and board[pawn_y - 2][pawn_x + 2] == "  ":
                    board[pawn_y][pawn_x] = "  "
                    board[pawn_y - 1][pawn_x + 1] = "  "
                    board[pawn_y - 2][pawn_x + 2] = "⚪"
                    print(f"White pawn {pawn_y}{pawn_x} eat Black Pawn {pawn_y-1}{pawn_x+1} and ends up at {pawn_y -2}{pawn_x + 2}") #✅ Checked
                else:
                    return False
            #Check if middle white pawn can eat
            elif ((pawn_x >= 2 and pawn_x <= 5) and pawn_y >= 2):  ##BUG NEED FIX
                if (board[pawn_y - 1][pawn_x + 1] == "⚫" and board[pawn_y - 2][pawn_x + 2] == "  ") or \
                    (board[pawn_y - 1][pawn_x - 1] == "⚫" and board[pawn_y - 2][pawn_x - 2] == "  "):
                    random_num = random.choice((0,1))
                    
                    #If 1 we eat top right if it's possible.
                    if random_num == 1:
                        if(board[pawn_y - 1][pawn_x + 1] == "⚫" and board[pawn_y - 2][pawn_x + 2] == "  "):
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y - 1][pawn_x + 1] = "  "
                            board[pawn_y - 2][pawn_x + 2] = "⚪"
                            print(f"White pawn {pawn_y}{pawn_x} eat Black Pawn {pawn_y-1}{pawn_x+1} and ends up at {pawn_y -2}{pawn_x + 2}") #✅ Checked
                        #Else we eat top left
                        elif (board[pawn_y - 1][pawn_x - 1] == "⚫" and board[pawn_y - 2][pawn_x - 2] == "  "):
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y - 1][pawn_x - 1] = "  "
                            board[pawn_y - 2][pawn_x - 2] = "⚪"                                                
                            print(f"White pawn {pawn_y}{pawn_x} eat Black Pawn {pawn_y-1}{pawn_x-1} and ends up at {pawn_y -2}{pawn_x - 2}") #✅ Checked
                            
                    #If 0 we eat top left if it's possible.
                    elif random_num == 0:
                        if(board[pawn_y - 1][pawn_x - 1] == "⚫" and board[pawn_y - 2][pawn_x - 2] == "  "):
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y - 1][pawn_x - 1] = "  "
                            board[pawn_y - 2][pawn_x - 2] = "⚪"
                            print(f"White pawn {pawn_y}{pawn_x} eat Black Pawn {pawn_y-1}{pawn_x-1} and ends up at {pawn_y -2}{pawn_x - 2}") #✅ Checked
                        #Else we eat bottom right.
                        elif(board[pawn_y - 1][pawn_x + 1] == "⚫" and board[pawn_y - 2][pawn_x + 2] == "  "):
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y - 1][pawn_x + 1] = "  "
                            board[pawn_y - 2][pawn_x + 2] = "⚪"
                            print(f"White pawn {pawn_y}{pawn_x} eat Black Pawn {pawn_y-1}{pawn_x+1} and ends up at {pawn_y -2}{pawn_x + 2}") #✅ Checked
                else:
                    return False
            #Check if most right white pawn can eat
            elif ((pawn_x == 7 or pawn_x == 6) and pawn_y >= 2):
                if board[pawn_y - 1][pawn_x - 1] == "⚫" and board[pawn_y - 2][pawn_x - 2] == "  ":
                    board[pawn_y][pawn_x] = "  "
                    board[pawn_y - 1][pawn_x - 1] = "  "
                    board[pawn_y - 2][pawn_x - 2] = "⚪"
                    print(f"White pawn {pawn_y}{pawn_x} eat Black Pawn {pawn_y-1}{pawn_x-1} and ends up at {pawn_y -2}{pawn_x - 2}") #✅ Checked
                else:
                    return False
        else:
            return False 
        
    def MoveCrownedPawn(self:object, board:list, turn:str)-> None:
        '''
        Function used to move crowned pawns. We'll select a random number from random_moves_list.
        List is filled with numbers going from 1 to 4.
        1 is TOP LEFT, 2 is TOP RIGHT, 3 is BOTTOM RIGHT, 4 is BOTTOM LEFT.
        Each pawn will have a different sized list depending on how many moves they can make.
        '''
        if turn == "White":
            if len(self.possible_movable_crowned_white_pawns) >= 1:
                random_pawn = random.choice(self.possible_movable_crowned_white_pawns)
                random_moves_list = self.AiMoveValidator.can_crowned_pawn_move(self.board,int(random_pawn[0]), int(random_pawn[1]))
                random_move = random.choice(random_moves_list)
                y = int(random_pawn[0])
                x = int(random_pawn[1])
                if random_move == 1: #Move TOP LEFT
                    board[y][x] = "  "
                    board[y-1][x-1] = "🤍"
                    print(f"Moving white_crowned_pawn [{y}{x}] to {y-1}{x-1} ")
                elif random_move == 2: #Move TOP RIGHT
                    board[y][x] = "  "
                    board[y-1][x+1] = "🤍"
                    print(f"Moving white_crowned_pawn [{y}{x}] to {y-1}{x+1} ")
                elif random_move == 3: #Move BOTTOM RIGHT
                    board[y][x] = "  "
                    board[y+1][x+1] = "🤍"
                    print(f"Moving white_crowned_pawn [{y}{x}] to {y+1}{x+1} ")
                elif random_move == 4: #Move BOTTOM LEFT
                    board[y][x] = "  "
                    board[y+1][x-1] = "🤍"
                    print(f"Moving white_crowned_pawn [{y}{x}] to {y+1}{x-1} ")

        elif turn == "Black":
            if len(self.possible_movable_crowned_black_pawns) >= 1:
                random_pawn = random.choice(self.possible_movable_crowned_black_pawns)
                random_moves_list = self.AiMoveValidator.can_crowned_pawn_move(self.board,int(random_pawn[0]), int(random_pawn[1]))
                random_move = random.choice(random_moves_list) ##BUG
                y = int(random_pawn[0])
                x = int(random_pawn[1])
                if random_move == 1: #Move TOP LEFT
                    board[y][x] = "  "
                    board[y-1][x-1] = "🖤"
                    print(f"Moving black_crowned_pawn [{y}{x}] to {y-1}{x-1} ")
                elif random_move == 2: #Move TOP RIGHT
                    board[y][x] = "  "
                    board[y-1][x+1] = "🖤"
                    print(f"Moving black_crowned_pawn [{y}{x}] to {y-1}{x+1} ")
                elif random_move == 3: #Move BOTTOM RIGHT
                    board[y][x] = "  "
                    board[y+1][x+1] = "🖤"
                    print(f"Moving black_crowned_pawn [{y}{x}] to {y+1}{x+1} ")
                elif random_move == 4: #Move BOTTOM LEFT
                    board[y][x] = "  "
                    board[y+1][x-1] = "🖤"
                    print(f"Moving black_crowned_pawn [{y}{x}] to {y+1}{x-1} ")

    def Crowned_Pawn_Eat(self:object, pawn_color:str, board:list)-> bool:
        """AI is creating summary for Crowned_Pawn_Eat

        Args:
            self (object): [description]
            pawn_color (str): [description]
            board (list): [description]

        Returns:
            bool: [description]
        """
        if pawn_color == "Black":
            random_crown = random.choice(self.possible_crowned_black_pawns_that_can_eat)
            pawn_y = int(random_crown[0])
            pawn_x = int(random_crown[1])
            color = "Black"
        elif pawn_color == "White":
            random_crown = random.choice(self.possible_crowned_white_pawns_that_can_eat)
            pawn_y = int(random_crown[0])
            pawn_x = int(random_crown[1])
            color = "White"
         #Controllo pedine X <= 1 E Y >= 6📌
        #Se x è compreso tra 0 e 1 e y >= 6 -> Queste pedine possono solo mangiare in alto a destra. #✅
        if pawn_y >= 6 and pawn_x <= 1:
            self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)
        #Controllo pedine X >= 6 E Y >= 6📌
        #Se x è maggiore uguale a 6 e y è maggiore uguale a 6 --> Queste pedine possono solo mangiare in alto a sinistra. ✅ -> cambiato <= 6 con >= 6
        elif pawn_x >= 6 and pawn_y >= 6:
            self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)
        #Controllo pedine X <= 1 E Y <= 1📌
        #Se x è <= 1 e y <= 1 --> Queste pedine possono solo mangiare in basso a destra. ✅
        elif pawn_x <= 1 and pawn_y <= 1:
            self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)
        #Controllo pedine X >= 6 e Y <= 1📌
        #Se x è >= 6 e y <= 1 --> Queste pedine possono solo mangiare in basso a sinistra. ✅
        elif pawn_x >= 6 and pawn_y <= 1:
            self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
        #Controllo pedine X <= 1 E Y >= 2 E Y <= 5📌
        #Se x <= 1 e Y compreso tra 2 e 5 --> Queste pedine possono mangiare sia in basso a destra che in alto a destra. ✅
        elif (pawn_x <= 1) and (pawn_y >= 2 and pawn_y <= 5):
            random_num = random.choice((0,1))
            
            if random_num == 0:
                if self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)
            elif random_num == 1:
                if self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)

        #Controllo pedine X >= 6 E Y >= 2 E Y <= 5📌
        # Se x è maggiore uguale a 6 e Y compreso tra 2 e 5 --> Queste pedine possono sia mangiare in basso che in alto a sinistra. ✅
        elif (pawn_x >= 6 ) and (pawn_y >= 2 and pawn_y <= 5):
            random_num = random.choice((0,1))
            if random_num == 0:
                if self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
            elif random_num == 1:
                if self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)

        #Controllo pedine X compreso tra 2 e 5 e Y maggiore uguale a 6📌
        #Se x è compreso tra 2 e 5 e y maggiore uguale a 6 --> Queste pedine possono solo mangiare in alto a destra o sinistra.✅
        elif (pawn_x >= 2 and pawn_x <= 5) and pawn_y >= 6:
            random_num = random.choice((0,1))
            if random_num == 0:
                if self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)
            elif random_num == 1:
                if self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)

        #Controllo pedine X compreso tra 2 e 5 e Y minore uguale a 1📌
        #Se x è compreso tra 2 e 5 e Y minore uguale a 1 --> Queste pedine possono solo mangiare in basso a destra o sinistra ✅
        elif (pawn_x >= 2 and pawn_x <= 5) and pawn_y <= 1:
            random_num = random.choice((0,1))
            if random_num == 0:
                if self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
            elif random_num == 1:
                if self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)

        #Controllo pedine X compreso tra 2 e 5 e Y compreso tra 2 e 5.📌
        #Se X è compreso tra 2 e 5 e Y è compreso tra 2 e 5 --> Queste pedine possono mangiare in ogni direzione.
        elif (pawn_x >= 2 and pawn_x <= 5) and (pawn_y >= 2 and pawn_y <= 5):
            random_num = random.choice((0,1,2,3))
            if random_num == 0:
                if self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
            elif random_num == 1:
                if self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)
            elif random_num == 2:
                if self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)
            elif random_num == 3:
                if self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomRight(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatBottomLeft(board,pawn_y,pawn_x,"Eat",color)
                elif self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Check",color):
                    self.DamaPawn.CrownEatTopRight(board,pawn_y,pawn_x,"Eat",color)