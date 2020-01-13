from piece import Piece
from move import Move

class Knight(Piece):
    def __init__(self, x = 0, y = 0, is_white = True):
        super().__init__(x, y, is_white)
    
    def base_value(self):
        return 3
        
    def moves(self, node):
        x,y = self.x - 2, self.y + 1
        if x > 0 and y < 8 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield Move(self, (self.x, self.y), (x, y))
        
        x,y = self.x - 2, self.y - 1
        if x > 0 and y > 0 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield Move(self, (self.x, self.y), (x, y))
            
        x,y = self.x + 2, self.y + 1
        if x < 8 and y < 8 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield Move(self, (self.x, self.y), (x, y))
        
        x,y = self.x + 2, self.y - 1
        if x < 8 and y > 0 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield Move(self, (self.x, self.y), (x, y))
            
        x,y = self.x - 1, self.y + 2
        if x > 0 and y < 8 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield Move(self, (self.x, self.y), (x, y))
        
        x,y = self.x - 1, self.y - 2
        if x > 0 and y > 0 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield Move(self, (self.x, self.y), (x, y))
            
        x,y = self.x + 1, self.y + 2
        if x < 8 and y < 8 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield Move(self, (self.x, self.y), (x, y))
        
        x,y = self.x + 1, self.y - 2
        if x < 8 and y > 0 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield Move(self, (self.x, self.y), (x, y))
            
    def attacks(self, node):
        x,y = self.x - 2, self.y + 1
        if x > 0 and y < 8 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield (x,y)
        
        x,y = self.x - 2, self.y - 1
        if x > 0 and y > 0 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield (x,y)
            
        x,y = self.x + 2, self.y + 1
        if x < 8 and y < 8 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield (x,y)
        
        x,y = self.x + 2, self.y - 1
        if x < 8 and y > 0 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield (x,y)
            
        x,y = self.x - 1, self.y + 2
        if x > 0 and y < 8 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield (x,y)
        
        x,y = self.x - 1, self.y - 2
        if x > 0 and y > 0 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield (x,y)
            
        x,y = self.x + 1, self.y + 2
        if x < 8 and y < 8 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield (x,y)
        
        x,y = self.x + 1, self.y - 2
        if x < 8 and y > 0 and ((piece := node.board[x + y * 8]) == None or piece.is_white != self.is_white):
            yield (x,y)