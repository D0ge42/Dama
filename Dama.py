import sys
from TurnHandler.TurnHandler import turnHandler
from Board.board import BoardClass
from Player.Human import HumanClass
from Player.Ai import AiClass
from DamaPawn.Damapawn import DamaPawnClass
from Referee.Referee import RefereeClass
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
        self.white_n = 0
        self.black_n = 0
        self.draw = 0
        self.n_available_white_moves = None
        self.n_available_white_pawns_that_can_eat = None
        self.possible_movable_crowned_white_pawns = None
        self.possible_white_crowned_pawns_that_can_eat = None
        
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
        self.Referee = RefereeClass()

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
        while self.partite_giocate < 1000:
        # while self.is_running:
                if turn == "White":
                    print()
                    print("⬜️ WHITE TURN ⬜️")
                    

                    #                         IT IS NOW WHITE TURN                              #
                    #---------------------------------------------------------------------------#


                    #                           AVAILABLE MOVES CHECK                           #
                    #---------------------------------------------------------------------------#
                    #Get number of available moves
                    self.n_available_white_moves = self.Ai.Available_white_pawn(self.board.board)[0]
                    self.n_available_white_pawns_that_can_eat = self.Ai.Available_white_pawn(self.board.board)[1]
                    self.possible_movable_crowned_white_pawns = self.Ai.Available_crowned_pawns(self.board.board, "White")[0]
                    self.possible_white_crowned_pawns_that_can_eat = self.Ai.Available_crowned_pawns(self.board.board, "White")[1]

                     
                    
                    #                       CHECK WIN CONDITION                                 #
                    #---------------------------------------------------------------------------#
                    draw = self.Referee.CheckDraw(self.total_moves,self.white_n,self.black_n)
                    if draw is True:
                        self.resetGame("Draw")

                    if self.Referee.CheckWin(
                        "White",
                        self.n_available_white_moves,
                        self.n_available_white_pawns_that_can_eat,
                        self.possible_movable_crowned_white_pawns,
                        self.possible_white_crowned_pawns_that_can_eat):

                            self.no_more_white_moves = True
                            self.white_cant_eat_anymore = True
                            print("👑BLACK PLAYER WINS!👑")
                            self.black_won += 1
                        
                        
                    #                      NO MOVES = RESTART GAME FROM 0                        #
                    #----------------------------------------------------------------------------#
                    #If there are no more moves the game stops and starts again.
                    if (self.no_more_white_moves and self.white_cant_eat_anymore) or \
                        (self.no_more_black_moves and self.black_cant_eat_anymore):


                        self.resetGame("")
                        #self.is_running = False
                        

                    #                             WHITE MOVES                                    #
                    #----------------------------------------------------------------------------#

                    # self.player1.Move(self.board.board)
                    print(f"📍Partita N°: {self.partite_giocate}")
                    random_num_w = random.choice((0,1,2,3))
                   
               

                    #Choose randomly between eat or move.
                    if random_num_w == 0:
                        if len(self.possible_white_crowned_pawns_that_can_eat):
                            self.Ai.Crowned_Pawn_Eat("White",self.board.board)
                        elif len(self.possible_movable_crowned_white_pawns):
                            self.Ai.MoveCrownedPawn(self.board.board,"White")
                        elif len(self.n_available_white_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "White")
                        elif len(self.n_available_white_moves):
                            self.Ai.Move(self.board.board, "White")

                    elif random_num_w == 1:
                        if len(self.possible_movable_crowned_white_pawns):
                            self.Ai.MoveCrownedPawn(self.board.board,"White")
                        elif len(self.possible_white_crowned_pawns_that_can_eat):
                            self.Ai.Crowned_Pawn_Eat("White",self.board.board)
                        elif len(self.n_available_white_moves):
                            self.Ai.Move(self.board.board, "White")
                        elif len(self.n_available_white_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "White")

                    elif random_num_w == 2:
                        if len(self.n_available_white_moves):
                            self.Ai.Move(self.board.board, "White")
                        elif len(self.n_available_white_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "White")
                        elif len(self.possible_white_crowned_pawns_that_can_eat):
                            self.Ai.Crowned_Pawn_Eat("White",self.board.board)
                        elif len(self.possible_movable_crowned_white_pawns):
                            self.Ai.MoveCrownedPawn(self.board.board,"White")

                    elif random_num_w == 3:
                        if len(self.n_available_white_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "White")
                        elif len(self.n_available_white_moves):
                            self.Ai.Move(self.board.board, "White")
                        elif len(self.possible_movable_crowned_white_pawns):
                            self.Ai.MoveCrownedPawn(self.board.board,"White")
                        elif len(self.possible_white_crowned_pawns_that_can_eat):
                            self.Ai.Crowned_Pawn_Eat("White",self.board.board)

                    self.DamaPawn.DamaCheck(self.board.board, "⚫",)
                    self.DamaPawn.DamaCheck(self.board.board, "⚪",)
                    print(f"📝Mosse fatte: {self.total_moves}")
                    self.white_n = self.board.white_pawns_n()
                    self.black_n = self.board.black_pawns_n()
                    self.board.print_board(self.board.board)
                    self.total_moves += 1

                    turn = "Black"
                    
                    #                       IT IS NOW BLACK TURN                                 #
                    #----------------------------------------------------------------------------#

                elif turn == "Black":
                    
                    print()
                    print("⬛️ BLACK TURN ⬛️")

                    #                         AVAILABLE MOVES CHECK                               #
                    #-----------------------------------------------------------------------------#
                    self.n_available_black_moves = self.Ai.Available_black_pawn(self.board.board)[0]
                    self.n_available_black_pawns_that_can_eat = self.Ai.Available_black_pawn(self.board.board)[1]
                    self.possible_movable_crowned_black_pawns = self.Ai.Available_crowned_pawns(self.board.board, "Black")[0]
                    self.possible_black_crowned_pawns_that_can_eat = self.Ai.Available_crowned_pawns(self.board.board, "Black")[1]
            
                    #                       CHECK WIN CONDITION                                   #
                    #-----------------------------------------------------------------------------#
                    draw = self.Referee.CheckDraw(self.total_moves,self.white_n,self.black_n)
                    if draw == True:
                        self.resetGame("Draw")


                    if self.Referee.CheckWin("Black",self.n_available_black_moves,
                                             self.n_available_black_pawns_that_can_eat,
                                             self.possible_movable_crowned_black_pawns,
                                            self.possible_black_crowned_pawns_that_can_eat):
                        
                        self.no_more_black_moves = True
                        self.black_cant_eat_anymore = True
                        print(f"👑WHITE PLAYER WINS!👑")
                        self.white_won += 1

                    
                    #                      NO MOVES = RESTART GAME FROM 0                        #
                    #----------------------------------------------------------------------------#

                    if (self.no_more_white_moves and self.white_cant_eat_anymore) or (self.no_more_black_moves and self.black_cant_eat_anymore):
                        #Calling a bord class will also refresh the board
                        self.resetGame("")
                        #self.is_running = False

                    #                          BLACK MOVES                                        #
                    #-----------------------------------------------------------------------------#
                    print(f"📍Partita N° : {self.partite_giocate}")
                    random_num = random.choice((0,1,2,3))
                
                    
                    #Choose randomly between eat and move.
                    if random_num == 0:
                        if len(self.possible_black_crowned_pawns_that_can_eat):
                            self.Ai.Crowned_Pawn_Eat("Black",self.board.board)
                        elif len(self.possible_movable_crowned_black_pawns):
                            self.Ai.MoveCrownedPawn(self.board.board,"Black")
                        elif len(self.n_available_black_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "Black")
                        elif len(self.n_available_black_moves):
                            self.Ai.Move(self.board.board, "Black")
                    elif random_num == 1:
                        if len(self.possible_movable_crowned_black_pawns):
                            self.Ai.MoveCrownedPawn(self.board.board,"Black")
                        elif len(self.possible_black_crowned_pawns_that_can_eat):
                            self.Ai.Crowned_Pawn_Eat("Black",self.board.board)
                        elif len(self.n_available_black_moves):
                            self.Ai.Move(self.board.board, "Black")
                        elif len(self.n_available_black_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "Black")

                    elif random_num == 2:
                        if len(self.n_available_black_moves):
                            self.Ai.Move(self.board.board, "Black")
                        elif len(self.n_available_black_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "Black")
                        elif len(self.possible_black_crowned_pawns_that_can_eat):
                            self.Ai.Crowned_Pawn_Eat("Black",self.board.board)
                        elif len(self.possible_movable_crowned_black_pawns):
                            self.Ai.MoveCrownedPawn(self.board.board,"Black")

                    elif random_num == 3:
                        if len(self.n_available_black_pawns_that_can_eat):
                            self.Ai.Eat(self.board.board, "Black")
                        elif len(self.n_available_black_moves):
                            self.Ai.Move(self.board.board, "Black")
                        elif len(self.possible_movable_crowned_black_pawns):
                            self.Ai.MoveCrownedPawn(self.board.board,"Black")
                        elif len(self.possible_black_crowned_pawns_that_can_eat):
                            self.Ai.Crowned_Pawn_Eat("Black",self.board.board)
                       
                    
                    
                    self.DamaPawn.DamaCheck(self.board.board, "⚫",)
                    self.DamaPawn.DamaCheck(self.board.board, "⚪",)
                    print(f"📝Mosse fatte: {self.total_moves}")
                    self.white_n = self.board.white_pawns_n()
                    self.black_n = self.board.black_pawns_n()
                    self.board.print_board(self.board.board)
                    self.total_moves += 1

                    turn = "White"

        print(f"🤍White won {self.white_won}🤍")
        print(f"🖤Black won: {self.black_won}🖤")
        print(f"🤝Draw: {self.draw}🤝")
            

    def resetGame(self:object,draw:str)-> None:
        self.board = BoardClass()
        self.no_more_white_moves = False
        self.no_more_black_moves = False
        self.white_cant_eat_anymore = False
        self.black_cant_eat_anymore = False
        if draw == "Draw":
            self.draw += 1
        self.total_moves = 0
        turn = self.turn_handler.randomTurn()
        self.partite_giocate += 1  