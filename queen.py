from piece import Piece
from move import Move

class Queen(Piece):
    def __init__(self, x=0, y=0, is_white=True):
        super().__init__(x, y, is_white, is_king=False)
        self.notation = "Q" if is_white else "q"
        
    def base_value(self):
        return 9
        
    def moves(self, node):
        # Rook moves
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
                
        # Bishop moves
        #Bottom-Left to Top-Right diagonal
        for x in range(self.x - 1, 0, -1):
            y = self.y + (x - self.x)
            if y >= 0:
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
                
        for x in range(self.x + 1, 8):
            y = self.y - (x - self.x)
            if y >= 0:
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
                
    def attacks(self, node):
        # Rook moves
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
        
        # Bishop moves
        #Bottom-Left to Top-Right diagonal
        for x in range(self.x - 1, 0, -1):
            y = self.y + (x - self.x)
            if y >= 0:
                piece = node.board[x + y * 8]
                if piece == None:
                    yield(x, y)
                elif piece.is_white != self.is_white:
                    yield (x, y)
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
                    yield (x, y)
                elif piece.is_white != self.is_white:
                    yield (x, y)
                    break
                else:
                    break
            else:
                break
        #Top-Left to Bottom-Right diagonal
        for x in range(self.x - 1, 0, -1):
            y = self.y - (x - self.x)
            if y < 8:
                piece = node.board[x + y * 8]
                if piece == None:
                    yield (x, y)
                elif piece.is_white != self.is_white:
                    yield (x, y)
                    break
                else:
                    break
            else:
                break
                
        for x in range(self.x + 1, 8):
            y = self.y - (x - self.x)
            if y >= 0:
                piece = node.board[x + y * 8]
                if piece == None:
                    yield (x, y)
                elif piece.is_white != self.is_white:
                    yield (x, y)
                    break
                else:
                    break
            else:
                break
        