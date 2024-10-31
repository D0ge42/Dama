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
        while self.is_running:
            if turn == "White":

                print("White TURN")
                self.player1.Move(self.board.board)
                self.board.print_board()
                turn = "Black"

            elif turn == "Black":

                print("Black TURN")
                possible_moves = self.Ai.Available_black_pawn_moves(self.board.board)
                self.Ai.Move(self.board.board,possible_moves)
                self.board.print_board()
                turn = "White"

