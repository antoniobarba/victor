from piece import Piece
from move import Move

class Rook(Piece):
    def __init__(self, x = 0, y = 0, is_white = True, not_moved_yet=True):
        super().__init__(x, y, is_white, is_king=False)
        self.not_moved_yet = not_moved_yet # Makes it easy to check for castling rights
        self.notation = "R"
        
    def base_value(self):
        return 5
        
    def moves(self, node):
        # to the left
        for x in range(self.x - 1, 0, -1):
            piece = node.board[x + self.y * 8]
            if piece == None:
                yield Move(self, (self.x, self.y), (x, self.y))
            elif piece.is_white != self.is_white:
                yield Move(self, (self.x, self.y), (x, self.y))
                break
            else:
                break
        
        # to the right
        for x in range(self.x + 1, 8):
            piece = node.board[x + self.y * 8]
            if piece == None:
                yield Move(self, (self.x, self.y), (x, self.y))
            elif piece.is_white != self.is_white:
                yield Move(self, (self.x, self.y), (x, self.y))
                break
            else:
                break
                
        # down
        for y in range(self.y - 1, 0, -1):
            piece = node.board[self.x + y * 8]
            if piece == None:
                yield Move(self, (self.x, self.y), (self.x, y))
            elif piece.is_white != self.is_white:
                yield Move(self, (self.x, self.y), (self.x, y))
                break
            else:
                break
        
        # up
        for y in range(self.y + 1, 8):
            piece = node.board[self.x + y * 8]
            if piece == None:
                yield Move(self, (self.x, self.y), (self.x, y))
            elif piece.is_white != self.is_white:
                yield Move(self, (self.x, self.y), (self.x, y))
                break
            else:
                break
        
    def attacks(self, node):
        # to the left
        for x in range(self.x - 1, 0, -1):
            piece = node.board[x + self.y * 8]
            if piece == None:
                yield (x, self.y)
            elif piece.is_white != self.is_white:
                yield (x, self.y)
                break
            else:
                break
        
        # to the right
        for x in range(self.x + 1, 8):
            piece = node.board[x + self.y * 8]
            if piece == None:
                yield (x, self.y)
            elif piece.is_white != self.is_white:
                yield (x, self.y)
                break
            else:
                break
                
        # down
        for y in range(self.y - 1, 0, -1):
            piece = node.board[self.x + y * 8]
            if piece == None:
                yield (self.x, y)
            elif piece.is_white != self.is_white:
                yield (self.x, y)
                break
            else:
                break
        
        # up
        for y in range(self.y + 1, 8):
            piece = node.board[self.x + y * 8]
            if piece == None:
                yield (self.x, y)
            elif piece.is_white != self.is_white:
                yield (self.x, y)
                break
            else:
                break
        
        