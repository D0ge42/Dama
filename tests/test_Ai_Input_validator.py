import unittest
from Board.board import BoardClass
from MoveValidator.AiMoveValidator import AiMoveValidatorClass

class TestGeneralInputValidator(unittest.TestCase):

    def setUp(self:object) -> None:
        self.AiMoveValidator = AiMoveValidatorClass()
        self.boardClass = BoardClass()
        self.board = self.boardClass.board

    def test_can_black_pawn_be_moved(self):
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