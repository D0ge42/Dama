import sys
from TurnHandler.TurnHandler import turnHandler
from Board.board import BoardClass
from Player.Human import HumanClass
from Player.Ai import AiClass
from DamaPawn.Damapawn import DamaPawnClass
import random

class DamaClass():
    '''Main class. It will handle the flow of the game.'''
    def __init__(self: object) -> None:
        self.is_running = True
        self.black_turn = False
        self.white_turn = False
        self.total_moves = 0
        self.no_more_white_moves = False
        self.white_cant_eat_anymore = False
        self.no_more_black_moves = False
        self.black_cant_eat_anymore = False
        self.partite_giocate = 0
        self.white_won = 0
        self.black_won = 0
        self.partite_giocate = 0

    def start_game(self: object)-> None:
        ''' Start game will handle:
            - Starting turn randomization
            - Board Update '''
        #Class istances
        self.turn_handler = turnHandler()
        self.board = BoardClass()
        self.player1 = HumanClass()
        self.Ai = AiClass()
        self.DamaPawn = DamaPawnClass()

        #-------------------------------------------#
        #             TURN SELECTION                #
        #-------------------------------------------#
        turn = self.turn_handler.randomTurn()

        #-------------------------------------------#
        #     PRINT STARTING BOARD                  #
        #-------------------------------------------#
        self.board.print_board(self.board.board)

        #-------------------------------------------#
        #               GAME FLOW                   # 
        #-------------------------------------------#
        while self.partite_giocate < 1:
        # while self.is_running:
                if turn == "White":
                    print()
                    print("White TURN")
                    

                    #                         IT IS NOW WHITE TURN                              #
                    #---------------------------------------------------------------------------#


                    #                           AVAILABLE MOVES CHECK                           #
                    #---------------------------------------------------------------------------#
                    #Get number of available moves
                    self.n_available_white_moves = self.Ai.Available_white_pawn(self.board.board)[0]
                    self.n_available_white_pawns_that_can_eat = self.Ai.Available_white_pawn(self.board.board)[1]
                    self.DamaPawn.DamaCheck(self.board.board, "⚫",)
                    
                    #                       CHECK WIN CONDITION                                 #
                    #---------------------------------------------------------------------------#
                    if len(self.n_available_white_moves) == 0 and len(self.n_available_white_pawns_that_can_eat) == 0:
                        self.no_more_white_moves = True
                        self.white_cant_eat_anymore = True
                        print("BLACK PLAYER WINS!")
                        self.black_won += 1
                        
                        
                    #                      NO MOVES = RESTART GAME FROM 0                        #
                    #----------------------------------------------------------------------------#
                    #If there are no more moves the game stops and starts again.
                    if (self.no_more_white_moves and self.white_cant_eat_anymore) or (self.no_more_black_moves and self.black_cant_eat_anymore):
                        #Calling board class will also refresh the board.
                        self.board = BoardClass()
                        self.no_more_white_moves = False
                        self.no_more_black_moves = False
                        self.white_cant_eat_anymore = False
                        self.black_cant_eat_anymore = False

                        self.total_moves = 0
                        turn = self.turn_handler.randomTurn()
                        self.partite_giocate += 1
                        #self.is_running = False
                        

                    #                             WHITE MOVES                                    #
                    #----------------------------------------------------------------------------#

                    # self.player1.Move(self.board.board)
                    print(f"Partita N° : {self.partite_giocate}")
                    random_tuple = (0,1)
                    random_num_w = random.choice(random_tuple)

                    #Choose randomly between eat or move.
                    if random_num_w == 1:
                        if len(self.n_available_white_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board,"White")
                        else:
                            self.Ai.Move(self.board.board, "White")
                    elif random_num_w == 0:
                        if len(self.n_available_white_moves):
                            self.Ai.Move(self.board.board, "White")
                        else:
                            self.Ai.Eat(self.board.board,"White")

                    print(f"Mosse fatte: {self.total_moves}")
                    self.board.white_pawns_n()
                    self.board.black_pawns_n()
                    self.board.print_board(self.board.board)
                    self.total_moves += 1

                    turn = "Black"
                    
                    #                       IT IS NOW BLACK TURN                                 #
                    #----------------------------------------------------------------------------#

                elif turn == "Black":
                    
                    print()
                    print("Black TURN")

                    #                         AVAILABLE MOVES CHECK                               #
                    #-----------------------------------------------------------------------------#
                    self.n_available_black_moves = self.Ai.Available_black_pawn(self.board.board)[0]
                    self.n_available_black_pawns_that_can_eat = self.Ai.Available_black_pawn(self.board.board)[1]

                    #                       CHECK WIN CONDITION                                   #
                    #-----------------------------------------------------------------------------#

                    if len(self.n_available_black_moves) == 0 and len(self.n_available_black_pawns_that_can_eat) == 0:
                        self.no_more_black_moves = True
                        self.black_cant_eat_anymore = True
                        print(f"WHITE PLAYER WINS!")
                        self.white_won += 1

                    
                    #                      NO MOVES = RESTART GAME FROM 0                        #
                    #----------------------------------------------------------------------------#

                    if (self.no_more_white_moves and self.white_cant_eat_anymore) or (self.no_more_black_moves and self.black_cant_eat_anymore):
                        #Calling a bord class will also refresh the board
                        self.board = BoardClass()
                        self.no_more_white_moves = False
                        self.no_more_black_moves = False
                        self.white_cant_eat_anymore  = False
                        self.black_cant_eat_anymore = False
                        self.total_moves = 0
                        turn = self.turn_handler.randomTurn()
                        self.partite_giocate += 1
                        #self.is_running = False

                    #                          BLACK MOVES                                        #
                    #-----------------------------------------------------------------------------#
                    print(f"Partita N° : {self.partite_giocate}")
                    random_tuple = (0,1)
                    random_num = random.choice(random_tuple)
                    
                    #Choose randomly between eat and move.
                    if random_num == 1:
                        if len(self.n_available_black_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "Black")
                        else:
                            self.Ai.Move(self.board.board, "Black")
                    elif random_num == 0:
                        if len(self.n_available_black_moves):
                            self.Ai.Move(self.board.board, "Black")
                        else:
                            self.Ai.Eat(self.board.board, "Black")
                    
                    print(f"Mosse fatte: {self.total_moves}")
                    self.board.white_pawns_n()
                    self.board.black_pawns_n()
                    self.board.print_board(self.board.board)
                    self.total_moves += 1

                    turn = "White"

        print(f"White won {self.white_won}")
        print(f"Black won: {self.black_won}")
            
        