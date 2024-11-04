import unittest
from Board.board import BoardClass
from Player.Ai import AiClass

class TestGeneralInputValidator(unittest.TestCase):

    def setUp(self:object) -> None:
        self.Ai = AiClass()
        self.boardClass = BoardClass()
        self.boardCLass = self.boardClass
        self.board = self.boardClass.board

    def test_available_black_pawn(self:object)->None:
        '''Function to test if available black pawn moves method works
           It should return a list of available pawns that are ready to be moved.'''

        #Starting list should be of len 4. Those are the available starting moves.
        list = self.Ai.Available_black_pawn(self.board)[0]
        if len(list) == 4:
            result = True
        else:
            result = False

        self.assertEqual(result, True)
#----                                       ----------------------------------#

        #If we move black pawn from [2][0] to [3][1] available move list len should be 5.
        self.board[2][0] = "  "
        self.board[3][1] = "⚫"
        list = self.Ai.Available_black_pawn(self.board)[0]
        if len(list) == 5:
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        #Reset board to start
        self.board[3][1] = "  "
        self.board[2][0] = "⚫"

#-----                                        ----------------------------------#

        #If we move black pawn from [2][6] to [3][7] we should free 2 pawns from moving.
        #List of available moves should be 6.
        self.board[2][6] = "  "
        self.board[3][7] = "⚫"
        list = self.Ai.Available_black_pawn(self.board)[0]
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
        list = self.Ai.Available_black_pawn(self.board)[0]
        if len(list) == 7:
            result = True
        else:
            result = False

        self.assertEqual(result, True)
        self.board[2][6] = "  "
        self.board[1][5] = "⚫"
#--------------------------------------------------------------------------------------------------#



   