import unittest
from Board.board import BoardClass
from MoveValidator.AiMoveValidator import AiMoveValidatorClass

class TestGeneralInputValidator(unittest.TestCase):

    def setUp(self:object) -> None:
        self.AiMoveValidator = AiMoveValidatorClass()
        self.boardClass = BoardClass()
        self.board = self.boardClass.board

    def test_can_black_pawn_be_moved(self)-> None:
        '''Test function to check if selected black pawn can move.
            Before reaching this function inside Ai Module, a check to see if selected pawn is black is made.'''
        black_pawn_y = 0
        black_pawn_x = 0 
        result = self.AiMoveValidator.can_black_pawn_be_moved(self.board,black_pawn_y, black_pawn_x)

        self.assertEqual(result, False)

        black_pawn_y = 2
        black_pawn_x = 0 
        result = self.AiMoveValidator.can_black_pawn_be_moved(self.board,black_pawn_y, black_pawn_x)

        self.assertEqual(result, True)

        black_pawn_y = 1
        black_pawn_x = 1 
        result = self.AiMoveValidator.can_black_pawn_be_moved(self.board,black_pawn_y, black_pawn_x)

        self.assertEqual(result, False)

        black_pawn_y = 2
        black_pawn_x = 6 
        result = self.AiMoveValidator.can_black_pawn_be_moved(self.board,black_pawn_y, black_pawn_x)

        self.assertEqual(result, True)
   
    def test_can_black_pawn_eat(self:object)-> None:
        '''
        Test function to check whether a given black pawn can eat a white pawn around it.
        '''

        #TEST MOST RIGHT PAWN EAT

        #First let's move pawns in a way we can test eat.
        self.board[2][6] = "  "
        self.board[3][7] = "⚫"

        self.board[5][5] = "  "
        self.board[4][6] = "⚪"

        print()
        #self.boardClass.print_board(self.board)

        #Function should return True since [3][7] black pawn can eat [4][6] white pawn.
        result = self.AiMoveValidator.can_black_pawn_eat("⚫", self.board,3,7)

        self.assertEqual(result, True)
        self.board = self.boardClass.clear_board(self.board) #restore board

#----        TEST MIDDLE BLACK PAWN EAT                 -----------------------#


        #First let's move pawns in a way we can test eat.
        self.board[2][6] = "  "
        self.board[3][5] = "⚫"

        #Move middle pawn top right
        self.board[5][3] = "  "
        self.board[4][4] = "⚪"
        #Move left white pawn top left
        self.board[5][7] = "  "
        self.board[4][6] = "⚪"

        #Function should return True.
        # [3][5] black pawn can eat [4][4] white pawn and [4][6] white pawn.
        result = self.AiMoveValidator.can_black_pawn_eat("⚫", self.board,3,5)

        self.assertEqual(result, True)
        self.board = self.boardClass.clear_board(self.board) #restore board

#----         TEST MOST LEFT BLACK PAWN EAT              ----------------------#

        
        #First let's move pawns in a way we can test eat.
        self.board[2][0] = "  "
        self.board[3][1] = "⚫"

        #Move middle pawn top right
        self.board[5][1] = "  "
        self.board[4][0] = "⚪"

        #Function should return False since [3][1] black pawn cannot eat [4][0] white pawn.
        #That's because the board would be out of range. 
        result = self.AiMoveValidator.can_black_pawn_eat("⚫", self.board,3,1)

        self.assertEqual(result, False)
        self.board = self.boardClass.clear_board(self.board) #restore board

    def test_can_white_pawn_eat(self:object)-> None:
        '''
        Test function to check whether a white pawn can eat a black pawn around it.
        '''
        #TEST MOST LEFT PAWN EAT

        #First let's move pawns in a way we can test eat.
        self.board[2][2] = "  "
        self.board[3][1] = "⚫"

        self.board[5][1] = "  "
        self.board[4][0] = "⚪"

        #Function should return True since [4][0] white pawn can eat [3][1] black pawn.
        result = self.AiMoveValidator.can_white_pawn_eat("⚪", self.board,4,0)

        self.assertEqual(result, True)
        self.board = self.boardClass.clear_board(self.board) #restore board

#------      TEST MIDDLE PAWN EAT                                       ---------------#


        #First let's move pawns in a way we can test eat.
        self.board[2][2] = "  "
        self.board[3][3] = "⚫"

        self.board[2][6] = "  "
        self.board[3][5] = "⚫"

        self.board[5][5] = "  "
        self.board[4][4] = "⚪"

        #Function should return True since [4][0] white pawn can eat [3][1] black pawn.
        result = self.AiMoveValidator.can_white_pawn_eat("⚪", self.board,4,4)

        self.assertEqual(result, True)
        self.board = self.boardClass.clear_board(self.board) #restore board

#------      TEST MOST RIGHT PAWN EAT                                    ---------------#


        #First let's move pawns in a way we can test eat.
        self.board[2][6] = "  "
        self.board[4][6] = "⚫"


        #Function should return True since [5][7] white pawn can eat [4][0] black pawn.
        result = self.AiMoveValidator.can_white_pawn_eat("⚪", self.board,5,7)

        self.assertEqual(result, True)
        self.board = self.boardClass.clear_board(self.board) #restore board

    def test_can_crowned_pawn_move(self:object)-> None:
        #We empty the board so we can test freely
        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 4 pawns around it.
        self.board[4][4] = "🤍"
        self.board[3][3] = "⚫"
        self.board[5][5] = "⚫"
        self.board[3][5] = "⚪"
        self.board[5][3] = "⚪"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,4,4)

        self.assertEqual(result, False)

#-------                                                              -------#
        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 3 pawns around it.
        #Top right spot is free so function should return a list equal to [2]
        self.board[4][4] = "🤍"
        self.board[3][3] = "⚫"
        self.board[5][5] = "⚫"
        self.board[5][3] = "⚪"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,4,4)

        self.assertEqual(result, [2])

#------                                                              -------#
        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 2 pawns around it.
        #Top right spot is free so function should return a list equal to [1,2]
        self.board[4][4] = "🤍"
        self.board[5][5] = "⚫"
        self.board[5][3] = "⚪"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,4,4)

        self.assertEqual(result, [1,2])

#-------                                                                -----#

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 1 pawns around it.
        #Top right spot is free so function should return a list equal to [1,2,3]
        self.board[4][4] = "🤍"
        self.board[5][3] = "⚪"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,4,4)

        self.assertEqual(result, [1,2,3])

#-------                                                                -----#

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 1 pawns around it.
        #Top right spot is free so function should return a list equal to [1,2,3,4]
        self.board[4][4] = "🤍"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,4,4)

        self.assertEqual(result, [1,2,3,4])
        

#-------                                                                -----#

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned black pawn at x == 7  and 2 pawns around it. One top left, one Bot left
        #Function should return False cause pawn cannot move.
        self.board[3][7] = "🖤"
        self.board[2][6] = "🤍"
        self.board[4][6] = "⚪"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,3,7)

        self.assertEqual(result, False)

#-------                                                                -----#

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned black pawn at x == 7  and 2 pawns around it. One top left, one Bot left
        #Function should return False cause pawn cannot move.
        self.board[3][7] = "🖤"
        self.board[4][6] = "⚪"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,3,7)

        self.assertEqual(result, [1]) 


#-------                                                                -----#

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned black pawn at x == 7  and 2 pawns around it. One top left, one Bot left
        #Function should return False cause pawn cannot move.
        self.board[3][7] = "🖤"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,3,7)

        self.assertEqual(result, [1,4]) 

#-------                                                                -----#
        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned black pawn at x == 7  and 2 pawns around it. One top left, one Bot left
        #Function should return False cause pawn cannot move.
        self.board[7][7] = "🖤"
        self.board[6][6] = "🤍"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_pawn_move(self.board,7,7)

        self.assertEqual(result, False)

    def test_can_crowned_eat(self:object)-> None:
        #We empty the board so we can test freely

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 4 pawns around it.
        self.board[4][4] = "🤍"
        self.board[3][3] = "⚫"
        self.board[5][5] = "⚫"
        self.board[3][5] = "⚪"
        self.board[5][3] = "⚪"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_eat("White",self.board,4,4)

        self.assertEqual(result, [1,3])
#-----                                                 #----------

        self.board = self.boardClass.empty_board(self.board)

        #Testing eat on board corners to see if pawn goes out of board
        self.board[1][6] = "🤍"
        self.board[0][5] = "⚫"
      
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_eat("White",self.board,1,6)

        self.assertEqual(result, False)
#-----                                                 #----------

        self.board = self.boardClass.empty_board(self.board)

        #Testing if pawn goes out of board when eating
        self.board[2][6] = "🖤"
        self.board[1][7] = "🤍"
      
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_eat("Black",self.board,2,6)

        self.assertEqual(result, False)
#-----                                                 #----------

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 4 pawns around it.
        self.board[4][4] = "🤍"
        self.board[3][3] = "⚫"
        self.board[5][5] = "⚫"
        self.board[3][5] = "⚫"
        self.board[5][3] = "⚫"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_eat("White",self.board,4,4)

        self.assertEqual(result, [1,2,3,4])
#-----                                                 #----------

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 4 pawns around it.
        self.board[4][4] = "🖤"
        self.board[3][3] = "⚫"
        self.board[5][5] = "⚫"
        self.board[3][5] = "⚫"
        self.board[5][3] = "⚫"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_eat("Black",self.board,4,4)

        self.assertEqual(result, False)
#-----                                                 #----------

        self.board = self.boardClass.empty_board(self.board)

        #We put a Crowned white pawn in the middle and 4 pawns around it.
        self.board[4][4] = "🖤"
        self.board[3][3] = "⚪"
        self.board[5][5] = "⚪"
        self.board[3][5] = "⚪"
        self.board[5][3] = "⚪"
        #self.boardClass.print_board(self.board)

        result = self.AiMoveValidator.can_crowned_eat("Black",self.board,4,4)

        self.assertEqual(result, [1,2,3,4])
#-----                                                 #----------

#--------------------------------------------------------------------------------------#
 