import unittest
from Board.board import BoardClass
from MoveValidator.GeneralMoveValidator import GeneralMoveValidatorClass

class TestGeneralInputValidator(unittest.TestCase):

    def setUp(self:object) -> None:
        self.GMoveValidator = GeneralMoveValidatorClass()
        self.boardClass = BoardClass()
        self.board = self.boardClass.board


    def test_check_user_input(self:object):
        '''
        Test function to check user input. 2 if user input is fine,
        0 if it contains also literal characters, 1 if it contains less/more than 2 digits.
        '''
        user_input = "42x"
        result = self.GMoveValidator.is_input_valid(user_input)

        self.assertEqual(result, 0)

        user_input = "42"
        result = self.GMoveValidator.is_input_valid(user_input)

        self.assertEqual(result, 2)

        user_input = "423"
        result = self.GMoveValidator.is_input_valid(user_input)

        self.assertEqual(result, 1)

        user_input = "38 "
        result = self.GMoveValidator.is_input_valid(user_input)

        self.assertEqual(result, 0)

    def test_is_pawn_in_range(self:object):
        '''Test function to see if pawn is in range. Before arriving at this function
           (inside Human Module), the input is filtered. Only digits, and must be 2 digits only.'''

        pawn_y = 7
        pawn_x = 7
        result = self.GMoveValidator.is_pawn_in_range(pawn_y, pawn_x)

        self.assertEqual(result, True)

        pawn_y = 7
        pawn_x = 8
        result = self.GMoveValidator.is_pawn_in_range(pawn_y, pawn_x)

        self.assertEqual(result, False)

        pawn_y = 8
        pawn_x = 7
        result = self.GMoveValidator.is_pawn_in_range(pawn_y, pawn_x)

        self.assertEqual(result, False)

        pawn_y = 0
        pawn_x = 0
        result = self.GMoveValidator.is_pawn_in_range(pawn_y, pawn_x)

        self.assertEqual(result, True)

    def test_is_spot_taken(self:object):
        '''Test function to see if a spot is taken. That means that pawn can't move on that spot.'''
        
        move_y = 5
        move_x = 1
        result = self.GMoveValidator.is_spot_taken(self.board, move_y, move_x)

        self.assertEqual(result, True)

        move_y = 4
        move_x = 0
        result = self.GMoveValidator.is_spot_taken(self.board, move_y, move_x)

        self.assertEqual(result, False)

        move_y = 2
        move_x = 0
        result = self.GMoveValidator.is_spot_taken(self.board, move_y, move_x)

        self.assertEqual(result, True)

        move_y = 4
        move_x = 6
        result = self.GMoveValidator.is_spot_taken(self.board, move_y, move_x)

        self.assertEqual(result, False)

    def test_is_move_in_range(self:object):

        move_y = 7
        move_x = 9
        result = self.GMoveValidator.is_move_in_range(move_y, move_x)

        self.assertEqual(result, False)

        move_y = 7
        move_x = 7
        result = self.GMoveValidator.is_move_in_range(move_y, move_x)

        self.assertEqual(result, True)

        move_y = 0
        move_x = 0
        result = self.GMoveValidator.is_move_in_range(move_y, move_x)

        self.assertEqual(result, True)

        move_y = 9
        move_x = 7
        result = self.GMoveValidator.is_move_in_range(move_y, move_x)

        self.assertEqual(result, False)