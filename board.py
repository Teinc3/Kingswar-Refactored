import pieces

class Board():

    def __init__(self):

        self.board = []

        # Create 5x4 board
        for i in range(5):
            row = []
            for i in range(4):
                row.append(None)
            self.board.append(row)
        
        # Place Kings and Rooks
        self.board[0][0] = pieces.Rook("white")
        self.board[4][3] = pieces.Rook("colored")

        self.board[1][1] = pieces.King("white")
        self.board[3][2] = pieces.King("colored")

    def print_board(self):
        # Print Buffer line
        buffer = "*" * 18
        print(buffer)
        
        # Print Board
        row_count = 1
        for row in self.board:
            print(str(row_count) + "|", end="")

            for piece in row:
                if piece == None:
                    print("   |", end="")
                else:
                    text = piece.name[0]
                    if piece.color == "colored":
                        text = '\033[34m' + text + '\033[0m'
                    print(" " + text + " |", end="")
            print()
            row_count += 1
        
        # Print Column Characters
        print("  ", end="")
        for i in range(4):
            print(" " + chr(i + 65) + "  ", end="")
        print()

        # Print Buffer line
        print(buffer)
    
def alphanum_to_index(alphanum):
    """
    Converts a string of length 2 or 4 to a list of integers representing the index of the board
    Accepted input: "(A-D)(1-5)(A-D)(1-5)" or "(A-D)(1-5)" (case insensitive) 
    Formula: index = (row - 1) * 4 + col - 1
    Example: 
    - "A1" -> [0]
    - "D5C3" -> [19, 14]
    - "c5d4" -> [18, 15]
    - "5" -> False
    """
    if len(alphanum) not in [2, 4]:
        return False
    elif len(alphanum) == 4:
        alphanum = [alphanum[0:2], alphanum[2:4]]
    else:
        alphanum = [alphanum]
    
    indices = []
    for item in alphanum:
        row = ord(item[0].upper()) - ord('A')
        col = int(item[1]) - 1
        if row < 0 or row > 3 or col < 0 or col > 4:
            return False
        index = (row * 5) + col
        indices.append(index)
    return indices