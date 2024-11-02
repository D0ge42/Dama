from Player.Player import PlayerClass
from MoveValidator.GeneralMoveValidator import GeneralMoveValidatorClass
from MoveValidator.PlayerMoveValidator import  PlayerMoveValidatorClass

class HumanClass(PlayerClass):
    def __init__(self:object)->None:
        self.GeneralMoveValidator = GeneralMoveValidatorClass()
        self.PlayerMoveValidator = PlayerMoveValidatorClass()

    def Move(self:object, board) -> None:
        ''' Handle player pawn movement. User input will have to run
        trough a MoveValidator before being consired a valid move.'''

        #Board
        self.board = board

        #--------------------------------------------------------------#
        #                        USER INPUT CHECKS                     #
        #--------------------------------------------------------------#

        #Ask user to choose a pawn to move  
        pawn = str(input(f"Choose which pawn to move(Y/X):  "))


        while self.GeneralMoveValidator.is_input_valid(pawn) == 0 or \
              self.GeneralMoveValidator.is_input_valid(pawn) == 1:
            pawn = str(input(f"Invalid input! Choose where to move selected pawn(Y/X):  "))
             
        #-----------------------------------------------------------------------#
        #                       SELECTED PAWN CHECKS                            #
        #-----------------------------------------------------------------------#

        #Range check
        while self.GeneralMoveValidator.is_pawn_in_range((int(pawn[0])), (int(pawn[1]))) == False:
            pawn = str(input(f"Not a valid range! Choose a white pawn to move(Y/X):  "))

        #Convert pawn string to pawn on board to pass it to the Validator.
        converted_pawn = self.board[int(pawn[0])][int(pawn[1])]
        
        #White pawn check
        while self.PlayerMoveValidator.is_pawn_white(converted_pawn) == False:
            pawn = str(input(f"Not a white pawn! Select a white pawn(Y/X):  "))
            converted_pawn = self.board[int(pawn[0])][int(pawn[1])]
        
        #Check if pawn can be moved
        while self.PlayerMoveValidator.can_white_pawn_be_moved(self.board,(int(pawn[0])),(int(pawn[1]))) == False:
            pawn = str(input(f"This pawn can't go anywhere. Choose another pawn(Y/X):  "))

        #------------------------------------------------------------------------#
        #                      USER INPUT CHECKS                                 #
        #------------------------------------------------------------------------#

        to = str(input(f"Choose where to move it(Y/X):  "))

        #Check if "to" is a valid input. 2 letters only digits.
        while self.GeneralMoveValidator.is_input_valid(to) == 0 or \
            self.GeneralMoveValidator.is_input_valid(to) == 1:
            to = str(input(f"Invalid input! Choose where to move selected pawn(Y/X):  "))

        #------------------------------------------------------------------------#
        #                      SELECTED MOVE CHECKS                              #
        #------------------------------------------------------------------------#

        #IsMoveInRange
        while self.GeneralMoveValidator.is_move_in_range(int(to[0]), int(to[1])) == False:
              to = str(input(f"Move Range out of bound! Please choose a valid move!(Y/X):  "))

        #Is move valid check
        while self.PlayerMoveValidator.validate_white_move(int(pawn),int(to)) == False:
            to = str(input(f"Invalid move! Choose where to move it(Y/X):  "))
        
        #Is spot already taken check
        while self.GeneralMoveValidator.is_spot_taken(self.board,int(to[0]),int(to[1])):
                    to = str(input(f"Spot already taken! Choose where to move your pawn(Y/X): "))
                    while self.PLayerMoveValidator.validate_white_move(int(pawn), int(to)) == False:
                         to = str(input(f"Invalid move! Choose where to move(Y/X):  "))

        #-------------------------------------------------------------------------#
        #                        MAKE THE MOVE                                    #
        #-------------------------------------------------------------------------#
        self.board[int(pawn[0])][int(pawn[1])] = "  "
        self.board[int(to[0])][int(to[1])] = "⚪"
        print(f"you moved {pawn[0]}{pawn[1]} to {to[0]}{to[1]}")
    
