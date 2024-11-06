class DamaPawnClass():
    def __init__(self) -> None:
        pass

    
    def DamaCheck(self:object,board:list, pawn_color:str): #✅
        '''
        Function to check if black or white pawns reached the opposite side.
        If so they should be crowned.
        '''
        for row_index, row in enumerate(board):
            for col_index, elem in enumerate(row):
                if elem == pawn_color and row_index == 7:
                    if pawn_color == "⚫":
                        board[row_index][col_index] = "🖤"
                elif elem == pawn_color and row_index == 0:
                    if pawn_color == "⚪":
                        board[row_index][col_index] = "🤍"

    def CrownEatTopRight(self:object,board:list, pawn_y:int, pawn_x:int,action:str,turn:str)-> bool:
        '''Eat top right'''
        if turn == "Black":
             eating_crown = "🖤"
             crown_pawn = "🤍"
             normal_pawn = "⚪"
        elif turn == "White":
             eating_crown = "🤍"
             crown_pawn = "🖤"
             normal_pawn = "⚫"
        if (board[pawn_y - 1][pawn_x + 1] == crown_pawn or board[pawn_y - 1][pawn_x + 1] == normal_pawn) and \
            board[pawn_y - 2][pawn_x + 2] == "  ":
                        if action == "Eat":
                            board[pawn_y][pawn_x] = "  "
                            board[pawn_y - 1][pawn_x + 1] = "  "
                            board[pawn_y - 2][pawn_x + 2] = eating_crown
                            if turn == "Black":
                                print(f"Black Crowned pawn [{pawn_y},{pawn_x}] eats [{pawn_y-1}{pawn_x+1}]")
                            else:
                                 print(f"White Crowned pawn [{pawn_y},{pawn_x}] eats [{pawn_y-1}{pawn_x+1}]")
                        elif action == "Check":
                            return True
        else:
              return False

    def CrownEatBottomRight(self:object, board:list, pawn_y:int, pawn_x:int, action:str,turn:str):
        if turn == "Black":
             eating_crown = "🖤"
             crown_pawn = "🤍"
             normal_pawn = "⚪"
        elif turn == "White":
             eating_crown = "🤍"
             crown_pawn = "🖤"
             normal_pawn = "⚫"
        if (board[pawn_y + 1][pawn_x + 1] == crown_pawn or board[pawn_y +1][pawn_x +1] == normal_pawn) and \
            board[pawn_y + 2][pawn_x + 2] == "  ":
                    if action == "Eat":
                        board[pawn_y][pawn_x] = "  "
                        board[pawn_y +1][pawn_x + 1] = "  "
                        board[pawn_y + 2][pawn_x + 2] = eating_crown
                        if turn == "Black":
                            print(f"Crowned pawn [{pawn_y},{pawn_x}] eats [{pawn_y+1}{pawn_x+1}]")
                        else:
                            print(f"White Crowned pawn [{pawn_y},{pawn_x}] eats [{pawn_y+1}{pawn_x+1}]")
                    elif action == "Check":
                        return True
        else:
              return False
    
    
    def CrownEatTopLeft(self:object, board:list, pawn_y:int, pawn_x:int, action:str,turn:str):
        if turn == "Black":
             eating_crown = "🖤"
             crown_pawn = "🤍"
             normal_pawn = "⚪"
        elif turn == "White":
             eating_crown = "🤍"
             crown_pawn = "🖤"
             normal_pawn = "⚫"
        if (board[pawn_y - 1][pawn_x - 1] == crown_pawn or board[pawn_y - 1][pawn_x - 1] == normal_pawn) and \
            board[pawn_y - 2][pawn_x - 2] == "  ":
                if action == "Eat":
                    board[pawn_y][pawn_x] = "  "
                    board[pawn_y - 1][pawn_x - 1] = "  "
                    board[pawn_y - 2][pawn_x - 2] = eating_crown
                    if turn == "Black":
                        print(f"Crowned pawn [{pawn_y},{pawn_x}] eats [{pawn_y-1}{pawn_x-1}]")
                    else:
                        print(f"White Crowned pawn [{pawn_y},{pawn_x}] eats [{pawn_y-1}{pawn_x-1}]")
                elif action == "Check":
                    return True
        else:
              return False
    
    def CrownEatBottomLeft(self:object, board:list, pawn_y:int, pawn_x:int, action:str,turn:str):
        if turn == "Black":
             eating_crown = "🖤"
             crown_pawn = "🤍"
             normal_pawn = "⚪"
        elif turn == "White":
             eating_crown = "🤍"
             crown_pawn = "🖤"
             normal_pawn = "⚫"
        if (board[pawn_y + 1][pawn_x - 1] == crown_pawn or board[pawn_y + 1][pawn_x -1] == normal_pawn) and \
            board[pawn_y + 2][pawn_x - 2] == "  ":
                    if action == "Eat":
                        board[pawn_y][pawn_x] = "  "
                        board[pawn_y + 1][pawn_x - 1] = "  "
                        board[pawn_y + 2][pawn_x - 2] = eating_crown
                        if turn == "Black":
                            print(f"Crowned pawn [{pawn_y},{pawn_x}] eats [{pawn_y+1}{pawn_x-1}]")
                        else:
                            print(f"White Crowned pawn [{pawn_y},{pawn_x}] eats [{pawn_y+1}{pawn_x-1}]")
                    elif action == "Check":
                        return True
        else:
              return False

    def CheckTopLeft(self:object,board:list,crown_y:int, crown_x:int)->bool:
        if (board[crown_y - 1][crown_x - 1] == "⚪") or (board[crown_y - 1][crown_x - 1] == "⚫")or \
            (board[crown_y - 1][crown_x- 1] == "🤍") or (board[crown_y - 1][crown_x - 1] == "🖤"):
                return False
        else:
                return True
           
    def CheckTopRight(self:object,board:list,crown_y:int, crown_x:int)->bool:
        if(board[crown_y -1][crown_x +1] == "⚪") or (board[crown_y -1][crown_x + 1] == "⚫") or \
            (board[crown_y -1][crown_x +1] == "🤍") or (board[crown_y -1][crown_x + 1] == "🖤"):
                return False
        else:
                return True
    
    def CheckBottomRight(self:object,board:list,crown_y:int, crown_x:int)->bool:
        if(board[crown_y +1][crown_x +1] == "⚪") or (board[crown_y +1][crown_x + 1] == "⚫") or \
            (board[crown_y + 1][crown_x +1] == "🤍") or (board[crown_y +1][crown_x + 1] == "🖤"):
            return False
        else:
            return True

    def CheckBottomLeft(self:object,board:list,crown_y:int, crown_x:int)->bool:
        if(board[crown_y +1][crown_x -1] == "⚪") or (board[crown_y +1][crown_x - 1] == "⚫") or \
            (board[crown_y + 1][crown_x -1] == "🤍") or (board[crown_y +1][crown_x - 1] == "🖤"):
            return False
        else:
            return True