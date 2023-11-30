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
        self.board[4][3] = pieces.Rook("black")

        self.board[1][1] = pieces.King("white")
        self.board[3][2] = pieces.King("black")

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
                    if piece.color == "black":
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