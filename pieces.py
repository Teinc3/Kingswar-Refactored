class Piece():

    def __init__(self, color, split):
        self.name = ""
        self.color = color
        self.split = split

    @staticmethod
    def destructure(start, end):
        """
        Destructures start and end into row and col
        """
        s_row = start // 4
        s_col = start % 4
        e_row = end // 4
        e_col = end % 4

        return s_row, s_col, e_row, e_col

class King(Piece):

    def __init__(self, color):
        super().__init__(color, False)
        self.name = "King"

    def can_move(self, board, start, end): # Check if King can move to index
        s_row, s_col, e_row, e_col = self.destructure(start, end)

        # Not implementing castling
        if s_row == e_row and s_col == e_col: # Did not move
            return False
        elif board.board[e_row][e_col] != None and not (board.board[e_row][e_col].color == self.color and self.name == board.board[e_row][e_col].name and self.split): # End is not empty
            return False
        elif abs(s_row - e_row) <= 1 and abs(s_col - e_col) <= 1:
            return True
        
        

class Rook(Piece):

    def __init__(self, color):
        super().__init__(color, False)
        self.name = "Rook"

    def can_move(self, board, start, end): # Check if Rook can move to index
        s_row, s_col, e_row, e_col = self.destructure(start, end)

        if s_row == e_row and s_col == e_col: # Did not move
            return False
        elif board.board[e_row][e_col] != None and not (board.board[e_row][e_col].color == self.color and self.name == board.board[e_row][e_col].name and self.split):
            return False
        else:
            if s_row == e_row:
                if s_col > e_col:
                    for i in range(e_col + 1, s_col):
                        if board.board[s_row][i] != None:
                            return False
                else:
                    for i in range(s_col + 1, e_col):
                        if board.board[s_row][i] != None:
                            return False
            elif s_col == e_col:
                if s_row > e_row:
                    for i in range(e_row + 1, s_row):
                        if board.board[i][s_col] != None:
                            return False
                else:
                    for i in range(s_row + 1, e_row):
                        if board.board[i][s_col] != None:
                            return False
            else:
                return False
            return True

