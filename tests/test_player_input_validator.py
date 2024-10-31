import unittest
from MoveValidator.PlayerMoveValidator import PlayerMoveValidatorClass
from Board.board import BoardClass

class TestPlayerInputValidator(unittest.TestCase):

    def setUp(self:object)-> None:
        '''Setup function will be called before every test'''
        self.PlayerValidator = PlayerMoveValidatorClass()
        self.boardClass = BoardClass()
        self.board = self.boardClass.board


    def test_if_pawn_is_white(self):
        '''Test function to check whether selected pawn is ⚪'''
        pawn = ""
        result = self.PlayerValidator.is_pawn_white(pawn)

        self.assertEqual(result, False)

        pawn = "1"
        result = self.PlayerValidator.is_pawn_white(pawn)

        self.assertEqual(result, False)

        pawn = "white"
        result = self.PlayerValidator.is_pawn_white(pawn)

        self.assertEqual(result, False)

        pawn = "£$&!&£/£/!/("
        result = self.PlayerValidator.is_pawn_white(pawn)

        self.assertEqual(result, False)

        pawn = "⚪"
        result = self.PlayerValidator.is_pawn_white(pawn)

        self.assertEqual(result, True)

        pawn = "⚫"
        result = self.PlayerValidator.is_pawn_white(pawn)

        self.assertEqual(result, False)

    def test_white_pawn_can_be_moved(self):
        '''Test function to check whether the selected pawn can be moved in any direction.'''
       
        white_pawn_y = 7
        white_pawn_x = 1
        result = self.PlayerValidator.can_white_pawn_be_moved(self.board, white_pawn_y, white_pawn_x)

        self.assertEqual(result, False)

        white_pawn_y = 7
        white_pawn_x = 7
        result = self.PlayerValidator.can_white_pawn_be_moved(self.board, white_pawn_y, white_pawn_x)

        self.assertEqual(result, False)

        white_pawn_y = 5
        white_pawn_x = 1
        result = self.PlayerValidator.can_white_pawn_be_moved(self.board, white_pawn_y, white_pawn_x)

        self.assertEqual(result, True)

        white_pawn_y = 2
        white_pawn_x = 0
        result = self.PlayerValidator.can_white_pawn_be_moved(self.board, white_pawn_y, white_pawn_x)

        self.assertEqual(result, False)

    def test_validate_white_move(self):
        '''Test function to check if selected move is diagonally valid.'''
        white_pawn = 51
        white_move = 40
        result = self.PlayerValidator.validate_white_move(white_pawn, white_move)

        self.assertEqual(result, True)

        white_pawn = 51
        white_move = 41
        result = self.PlayerValidator.validate_white_move(white_pawn, white_move)

        self.assertEqual(result, False)

        white_pawn = 57
        white_move = 46
        result = self.PlayerValidator.validate_white_move(white_pawn, white_move)

        self.assertEqual(result, True)

        white_pawn = 22
        white_move = 33
        result = self.PlayerValidator.validate_white_move(white_pawn, white_move)

        self.assertEqual(result, False)
