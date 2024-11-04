from Player.Player import PlayerClass
from MoveValidator.AiMoveValidator import AiMoveValidatorClass
import random

class AiClass(PlayerClass):
    def __init__(self:object)-> None:
        self.AiMoveValidator = AiMoveValidatorClass()


    def Available_black_pawn(self:object, board:list) -> list:
        '''Function that will check available black pawns'''
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
            print(f"Mosse nere disponibili: {len(self.possible_movable_black_pawns)}")
            if len(self.possible_movable_black_pawns) >= 1:
                self.move_to_do_black = random.choice(self.possible_movable_black_pawns)
                if board[int(self.move_to_do_black[0])][int(self.move_to_do_black[1])] == "⚫":
                    self.AiMoveValidator.Available_pawn_moves(self.board,"⚫",int(self.move_to_do_black[0]), int(self.move_to_do_black[1]))

        elif turn == "White":
            print(f"Mosse bianche disponibili: {len(self.possible_movable_white_pawns)}")
            if len(self.possible_movable_white_pawns) >= 1:
                self.move_to_do_white = random.choice(self.possible_movable_white_pawns)
                if board[int(self.move_to_do_white[0])][int(self.move_to_do_white[1])] == "⚪":
                        self.AiMoveValidator.Available_pawn_moves(self.board,"⚪",int(self.move_to_do_white[0]), int(self.move_to_do_white[1]))

    def Eat(self:object, board:list, turn:str)-> None:
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
                return
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
                    random_tuple = (0,1)
                    random_num_b = random.choice(random_tuple)
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
                    random_tuple = (0,1)
                    random_num = random.choice(random_tuple)
                    
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