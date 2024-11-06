import unittest
from Referee.Referee import RefereeClass

class TestReferee(unittest.TestCase):

    def setUp(self:object)-> None:
        '''Setup function will be called before every test'''
        self.referee = RefereeClass()

    
    def testDraw(self:object)-> None:
        self.referee.CheckDraw(50,12,12)
