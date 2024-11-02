import unittest
from Board.board import BoardClass
from Player.Ai import AiClass
from Ai_utility.Ai_Utility import AiUtility

class TestGeneralInputValidator(unittest.TestCase):

    def setUp(self:object) -> None:
        self.Ai = AiClass()
        self.boardClass = BoardClass()
        self.AiUtility = AiUtility()
        self.boardCLass = self.boardClass
        self.board = self.boardClass.board

    def test_available_black_pawn(self:object)->None:
        '''Function to test if available black pawn moves method works
           It should return a list of available pawns that are ready to be moved.'''

        #Starting list should be of len 4. Those are the available starting moves.
        list = self.Ai.Available_black_pawn(self.board)
        if len(list) == 4:
            result = True
        else:
            False

        self.assertEqual(result, True)
#----                                       ----------------------------------#

        #If we move black pawn from [2][0] to [3][1] available move list len should be 5.
        self.board[2][0] = "  "
        self.board[3][1] = "⚫"
        list = self.Ai.Available_black_pawn(self.board)
        if len(list) == 5:
            result = True
        else:
            False

        self.assertEqual(result, True)
        #Reset board to start
        self.board[3][1] = "  "
        self.board[2][0] = "⚫"

#-----                                        ----------------------------------#

        #If we move black pawn from [2][6] to [3][7] we should free 2 pawns from moving.
        #List of available moves should be 6.
        self.board[2][6] = "  "
        self.board[3][7] = "⚫"
        list = self.Ai.Available_black_pawn(self.board)
        if len(list) == 6:
            result = True
        else:
            False

        self.assertEqual(result, True)
#-----                                            ----------------------------------------------#
        #Without resetting board we make a double move. 
        # First move is [2][6] in [3][7] made in previous test
        # Second move is [1][5] in [2][6]
        #Result should be a list of 7 available pawns to move.

        self.board[1][5] = "  "
        self.board[2][6] = "⚫"
        list = self.Ai.Available_black_pawn(self.board)
        if len(list) == 7:
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        self.board[2][6] = "  "
        self.board[1][5] = "⚫"
#--------------------------------------------------------------------------------------------------#



    def test_available_pawn_moves(self:object)-> None:
        '''
        Test function to check if random moves for respective pawn color is working.
        Given pawns will all have at least one available moves.
        We're not considering pawns that can't move because those are excluded by previous Method.
        '''
        #Check middle black pawns
        self.AiUtility.Available_pawn_moves(self.board,"⚫", 2,2)
        #If the spot where the pawn was is blank and either bottom right or left is black
        #Result will be true and given method works.
        if (self.board[2][2] == "  " and (self.board[3][1] == "⚫" or self.board[3][3] == "⚫")):
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        #Clear board
        self.boardClass.clear_board(self.board)
#--------                                       -----------------------------------#
        #Check left black pawns
        self.AiUtility.Available_pawn_moves(self.board,"⚫", 2,0)
        #Black Pawn at most left spot can only move bottom right. So it should be +1 +1 to Y and X.
        #Also starting spot will be blank.
        #If so Result will be true and given method works.
        if (self.board[2][0] == "  " and (self.board[3][1] == "⚫" )):
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        #Clear board
        self.boardClass.clear_board(self.board)

#-------                                         ----------------------------------#

        #Check right black pawns
        #First we'll have to move a pawn in that spot.
        self.board[2][6] = "  "
        self.board[3][7] = "⚫"
        self.AiUtility.Available_pawn_moves(self.board,"⚫", 3,7)
        #Black Pawn at most right spot can only move bottom left. So it should be +1 -1 to Y and X.
        #Also starting spot will be blank.
        #If so Result will be true and given method works.
        if (self.board[3][7] == "  " and (self.board[4][6] == "⚫" )):
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        #Clear board
        self.boardClass.clear_board(self.board)

#-------                                         ----------------------------------#

        #Check middle white  pawns
        self.AiUtility.Available_pawn_moves(self.board,"⚪", 5,3)
        #For middle pawn there might be 2 possible moves. So we'll check both and if one of these spot is white the method worked.
        #We'll also have to check that starting spot is blank after move.
        #If so Result will be true and given method works.
        if (self.board[5][3] == "  " and (self.board[4][2] == "⚪" ) or (self.board[4][4] == "⚪" )):
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        #Clear board
        self.boardClass.clear_board(self.board)

#-------                                         ----------------------------------#

        #Check left white  pawns
        #First we'll have to move a pawn at most left spot.
        self.board[5][1] = "  "
        self.board[4][0] = "⚪"
        self.AiUtility.Available_pawn_moves(self.board,"⚪", 4,0)
        #Most left white pawn can only move top right. That means Y - 1 and X + 1 
        #We'll also check that starting spot is blank after move.
        #If so Result will be true and given method works.
        if (self.board[4][0] == "  " and (self.board[3][1] == "⚪" )): 
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        #Clear board
        self.boardClass.clear_board(self.board)
#-------                                         ----------------------------------#

        #Check left white  pawns
        self.AiUtility.Available_pawn_moves(self.board,"⚪", 5,7)
        #Most right pawn can only move top left, that means Y - 1 AND X - 1
        #We'll also check that starting spot is blank after move.
        #If so Result will be true and given method works.
        if (self.board[5][7] == "  " and (self.board[4][6] == "⚪" )): 
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        #Clear board
        self.boardClass.clear_board(self.board)

#--------------------------------------------------------------------------------------#
