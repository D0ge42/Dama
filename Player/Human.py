from Player.Player import PlayerClass
from MoveValidator.MoveValidator import MoveValidatorClass

class HumanClass(PlayerClass):
    def __init__(self:object)->None:
        self.MoveValidator = MoveValidatorClass()

    def Move(self:object, board) -> None:
        ''' Handle player pawn movement. User input will have to run
        trough a MoveValidator before being consired a valid move.'''

        #Board
        self.board = board

        #Ask user to choose a pawn to move  
        pawn = str(input(f"Choose which pawn to move(Y/X):  "))

        #Input lenght check
        while(len(pawn)) is not 2:
             pawn = str(input(f"Choose which pawn to move(Y/X):  "))
             
             

        #Convert pawn string to pawn on board to pass it to the Validator.
        converted_pawn = self.board[int(pawn[0])][int(pawn[1])]
        
        #-----------------------------------------------------------------------#
        #                       SELECTED PAWN CHECKS                            #
        #-----------------------------------------------------------------------#

        #Range check
        while self.MoveValidator.is_pawn_in_range((int(pawn[0])), (int(pawn[1]))) == False:
            pawn = str(input(f"Not a valid range! Choose a white pawn to move(Y/X):  "))
        #White pawn check
        while self.MoveValidator.is_pawn_white(converted_pawn) == False:
            pawn = str(input(f"Not a white pawn! Select a white pawn(Y/X):  "))
            converted_pawn = self.board[int(pawn[0])][int(pawn[1])]
        
        #Check if pawn can be moved
        while self.MoveValidator.can_pawn_be_moved(self.board,(int(pawn[0])),(int(pawn[1]))) == False:
            pawn = str(input(f"This pawn can't go anywhere. Choose another pawn(Y/X):  "))

        #------------------------------------------------------------------------#
        #                      SELECTED MOVE CHECKS                              #
        #------------------------------------------------------------------------#

        #Where to move selected pawns
        to = str(input(f"Choose where to move it(Y/X):  "))

        #Is move valid check
        while self.MoveValidator.validate_white_move(int(pawn),int(to)) == False:
            to = str(input(f"Invalid move! Choose where to move it(Y/X):  "))
        
        #Is spot already taken check
        while self.MoveValidator.is_spot_taken(self.board,int(to[0]),int(to[1])):
                    to = str(input(f"Spot already taken! Choose where to move your pawn(Y/X): "))
                    while self.MoveValidator.validate_white_move(int(pawn), int(to)) == False:
                         to = str(input(f"Invalid move! Choose where to move(Y/X):  "))

        #-------------------------------------------------------------------------#
        #                        MAKE THE MOVE                                    #
        #-------------------------------------------------------------------------#
        self.board[int(pawn[0])][int(pawn[1])] = "  "
        self.board[int(to[0])][int(to[1])] = "⚪"
        print(f"you moved {pawn[0]}{pawn[1]} to {to[0]}{to[1]}")
    
