
class RefereeClass():
    def __init__(self:object)-> None:
        self.previous_number = 0
        self.saved_number_black_pawns = 0
        self.saved_number_white_pawns = 0

    def CheckWin(self,which_player:str,moves:list,eat:list,crowned_moves:list,crowned_eat):
        if (which_player) == "White":
            if len(moves) + len(eat) + len(crowned_moves) + len(crowned_eat) == 0:
                return True
            else:
                return False
        elif (which_player) == "Black":
            if len(moves) + len(eat) + len(crowned_moves) + len(crowned_eat)== 0:
                return True
            else:
                return False


    def CheckDraw(self, current_move_number: int, white_pawns: int, black_pawns: int):
        '''Function to check if the game is a draw. If no pawns have been captured within 50 moves,
            then it is considered a draw.'''
        # Check every 50 moves
        if self.previous_number == current_move_number - 50:
            if self.saved_number_black_pawns == black_pawns and \
               self.saved_number_white_pawns == white_pawns:
                print("Draw")
                return True
        
        # Save the number of pawns every 50 moves
        elif current_move_number % 50 == 0:
            self.previous_number = current_move_number
            self.saved_number_white_pawns = white_pawns
            self.saved_number_black_pawns = black_pawns