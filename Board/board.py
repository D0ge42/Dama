from Player.Human import HumanClass

class BoardClass():
    #Generate 8 x 8 matrix of available slots using nested list comprehension.
    def __init__(self:object) -> None:
        self.board = [['⚫' if (r%2 == 0 and c%2 == 0 and c < 3) or (r%2 != 0 and c%2 != 0 and c < 3)
                            else '⚪' if (r%2 == 0 and c%2 == 0 and c > 4) or (r%2 != 0 and c%2 != 0 and c > 4)
                            else '  ' if (r%2 != 0 and c%2 == 0) or (r%2 == 0 and c%2 != 0)
                            else '  ' for r in range(0,8)] for c in range(0,8)]


    def print_board(self:object):
        ''' Convert self.board matrix into a human-readable form using strings and prints it'''
        i = 0
        print("   0️⃣    1️⃣    2️⃣    3️⃣    4️⃣    5️⃣    6️⃣    7️⃣")
        print()
        for row in self.board:
            print(f"{i}  " + " | ".join(str(elem) for elem in row))
            print("-" * 42)
            i += 1
        print()


    def print_move(self:object,x:int,y:int)-> None:
        '''Test function to check wheter it's possible to move the  '''
        print(self.board[x][y])

    def clear_board(self:object, board:list)->None:
         board = [['⚫' if (r%2 == 0 and c%2 == 0 and c < 3) or (r%2 != 0 and c%2 != 0 and c < 3)
                            else '⚪' if (r%2 == 0 and c%2 == 0 and c > 4) or (r%2 != 0 and c%2 != 0 and c > 4)
                            else '  ' if (r%2 != 0 and c%2 == 0) or (r%2 == 0 and c%2 != 0)
                            else '  ' for r in range(0,8)] for c in range(0,8)]
