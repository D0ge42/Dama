import sys
from TurnHandler.TurnHandler import turnHandler
from Board.board import BoardClass
from Player.Human import HumanClass
from Player.Ai import AiClass

class DamaClass():
    '''Main class. It will handle the flow of the game.'''
    def __init__(self: object) -> None:
        self.is_running = True
        self.black_turn = False
        self.white_turn = False
        self.total_moves = 0
        self.no_more_white_moves = False
        self.no_more_black_moves = False
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

        #-------------------------------------------#
        #             TURN SELECTION                #
        #-------------------------------------------#
        turn = self.turn_handler.randomTurn()

        #-------------------------------------------#
        #     PRINT STARTING BOARD                  #
        #-------------------------------------------#
        self.board.print_board()

        #-------------------------------------------#
        #               GAME FLOW                   # 
        #-------------------------------------------#
        while self.partite_giocate <= 10000:
        # while self.is_running:
                if turn == "White":
                    print("White TURN")

                    #                           AVAILABLE MOVES CHECK                           #
                    #---------------------------------------------------------------------------#
                    #Get number of available moves
                    self.n_available_white_moves = self.Ai.Available_white_pawn(self.board.board)
                    #If there are 0 white pawns available to move it's black turn
                    if len(self.n_available_white_moves) == 0:
                        self.no_more_white_moves = True
                        turn = "Black"
                        
                    #                      NO MOVES = RESTART GAME FROM 0                        #
                    #----------------------------------------------------------------------------#
                    #If there are no more moves the game stops and starts again.
                    if self.no_more_white_moves and self.no_more_black_moves:
                        #Calling board class will also refresh the board.
                        self.board = BoardClass()
                        self.no_more_white_moves = False
                        self.no_more_black_moves = False
                        self.total_moves = 0
                        turn = self.turn_handler.randomTurn()
                        self.partite_giocate += 1
                        #self.is_running = False
                        

                    #                             WHITE MOVES                                    #
                    #----------------------------------------------------------------------------#

                    # self.player1.Move(self.board.board)
                    # self.Ai.Eat(self.board.board, "⚪")
                    self.Ai.Move(self.board.board, "White")
                    self.board.print_board()
                    self.total_moves += 1

                    print(f"Mosse fatte: {self.total_moves}")
                    turn = "Black"
                    
                    #                              TURN SWITCH                                   #
                    #----------------------------------------------------------------------------#

                elif turn == "Black":

                    print("Black TURN")

                    #                         AVAILABLE MOVES CHECK                               #
                    #-----------------------------------------------------------------------------#
                    self.n_available_black_moves = self.Ai.Available_black_pawn(self.board.board)
                    
                    print(len(self.n_available_black_moves))

                    if len(self.n_available_black_moves) == 0:
                        self.no_more_black_moves = True
                        turn = "White"
                    
                    #                      NO MOVES = RESTART GAME FROM 0                        #
                    #----------------------------------------------------------------------------#

                    if self.no_more_white_moves and self.no_more_black_moves:
                        #Calling a bord class will also refresh the board
                        self.board = BoardClass()
                        self.no_more_white_moves = False
                        self.no_more_black_moves = False
                        self.total_moves = 0
                        turn = self.turn_handler.randomTurn()
                        self.partite_giocate += 1
                        #self.is_running = False

                    #                          BLACK MOVES                                        #
                    #-----------------------------------------------------------------------------#
                    
                    self.Ai.Move(self.board.board, "Black")
                    self.board.print_board()
                    self.total_moves += 1
                    print(f"Mosse fatte: {self.total_moves}")

                    turn = "White"

                print(f"Partite giocate: {self.partite_giocate}")