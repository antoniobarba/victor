class Piece:
    def __init__(self, x=0, y=0, is_white=True, is_king=False):
        self.x = x
        self.y = y
        self.is_white = is_white
        self.is_king = is_king

    def base_value(self):
        raise Exception("Not Implemented Here")

    def moves(self, node):
        raise Exception("Not Implemented Here")
