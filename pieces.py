class Piece():

    def __init__(self, color, split):
        self.name = ""
        self.color = color
        self.split = split


class King(Piece):

    def __init__(self, color):
        super().__init__(color, False)
        self.name = "King"

    def can_move(self, board, x, y):
        pass

class Rook(Piece):

    def __init__(self, color):
        super().__init__(color, False)
        self.name = "Rook"