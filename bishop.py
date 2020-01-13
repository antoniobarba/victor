from piece import Piece
from move import Move

class Bishop(Piece):
    def __init__(self, x=0, y=0, is_white=True):
        super().__init__(x, y, is_white, is_king=False)
        
    def base_value(self):
        return 3
        
    def moves(self, node):
        #Bottom-Left to Top-Right diagonal
        for x in range(self.x - 1, 0, -1):
            y = self.y + (x - self.x)
            if y > 0:
                piece = node.board[x + y * 8]
                if piece == None:
                    yield Move(self, (self.x, self.y), (x, y))
                elif piece.is_white != self.is_white:
                    yield Move(self, (self.x, self.y), (x, y))
                    break
                else:
                    break
            else:
                break
                
        for x in range(self.x + 1, 8):
            y = self.y + (x - self.x)
            if y < 8:
                piece = node.board[x + y * 8]
                if piece == None:
                    yield Move(self, (self.x, self.y), (x, y))
                elif piece.is_white != self.is_white:
                    yield Move(self, (self.x, self.y), (x, y))
                    break
                else:
                    break
            else:
                break
        #Top-Left to Bottom-Right diagonal
        for x in range(self.x - 1, 0, -1):
            y = self.y - (x - self.x)
            if y > 0:
                piece = node.board[x + y * 8]
                if piece == None:
                    yield Move(self, (self.x, self.y), (x, y))
                elif piece.is_white != self.is_white:
                    yield Move(self, (self.x, self.y), (x, y))
                    break
                else:
                    break
            else:
                break
                
        for x in range(self.x + 1, 8):
            y = self.y - (x - self.x)
            if y < 8:
                piece = node.board[x + y * 8]
                if piece == None:
                    yield Move(self, (self.x, self.y), (x, y))
                elif piece.is_white != self.is_white:
                    yield Move(self, (self.x, self.y), (x, y))
                    break
                else:
                    break
            else:
                break