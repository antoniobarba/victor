from piece import Piece
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from move import Move

class Pawn(Piece):
    def __init__(self, x=0, y=0, is_white=True, enpassant_rule_active=False):
        super().__init__(x, y, is_white, is_king=False)
        self.enpassant_rule_active = enpassant_rule_active
        self.notation = "p"

    def base_value(self):
        return 1

    def moves(self, node):
        if self.is_white:
            direction = 1
        else:
            direction = -1
            
        if (self.is_white and self.y < 6) or (not self.is_white and self.y > 1):
            # Go up
            newx, newy = self.x, self.y + 1 * direction
            if node.board[newx + newy*8] == None:
                yield Move(Pawn(self, newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                
            # Go up 2 squares on the first move
            newx, newy = self.x, self.y + 2 * direction
            if ((self.is_white and self.y == 1) or (not self.is_white and self.y == 6)) and node.board[newx + newy * 8] == None:
                yield Move(Pawn(self, newx, newy, enpassant_rule_active=True, is_white=self.is_white), (self.x, self.y), (newx, newy))
                
            # Take left
            newx, newy = self.x - 1, self.y + 1 * direction
            if self.x > 0 and (piece := node.board[newx + self.y * 8]) != None and piece.is_white != self.is_white:
                yield Move(Pawn(self, newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
            # Take left enpassant
            if self.x > 0 and (piece := node.board[newx + self.y * 8]) != None and piece.is_white != self.is_white:
                if isinstance(piece, Pawn):
                    if piece.enpassant_rule_active:
                        yield Move(Pawn(self, newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy), enpassant=True)
                
            # Take right
            newx, newy = self.x + 1, self.y + 1 * direction
            if self.x < 7 and (piece := node.board[newx + self.y * 8]) != None and piece.is_white != self.is_white:
                yield Move(Pawn(self, newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
            # Take right enpassant
            if self.x < 7 and (piece := node.board[newx + self.y * 8]) != None and piece.is_white != self.is_white:
                if isinstance(piece, Pawn):
                    if piece.enpassant_rule_active:
                        yield Move(Pawn(self, newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy), enpassant=True)
            
            
        if (self.is_white and self.y == 6) or (not self.is_white and self.y == 1):
            # Go up with promotion
            newx, newy = self.x, self.y + 1 * direction
            if node.board[newx + newy*8] == None:
                yield Move(Knight(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Queen(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Rook(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Bishop(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                
            # Take left with promotion
            newx, newy = self.x - 1, self.y + 1 * direction
            if self.x > 0 and (piece := node.board[newx + newy * 8] != None) and piece.is_white != self.is_white:
                yield Move(Knight(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Queen(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Rook(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Bishop(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                
            # Take right with promotion
            newx, newy = self.x + 1, self.y + 1 * direction
            if self.x < 7 and (piece := node.board[newx + newy * 8] != None) and piece.is_white != self.is_white:
                yield Move(Knight(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Queen(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Rook(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                yield Move(Bishop(newx, newy, is_white=self.is_white), (self.x, self.y), (newx, newy))
                    
    def attacks(self, node):
        if self.is_white:
            x,y = self.x - 1, self.y + 1
            if x >= 0 and y < 8:
                yield (x, y)
                
            x,y = self.x + 1, self.y + 1
            if x < 8 and y < 8:
                yield (x, y)
        else:
            x,y = self.x - 1, self.y - 1
            if x >= 0 and y >= 0:
                yield (x, y)
            
            x,y = self.x + 1, self.y - 1
            if x < 8 and y >= 0:
                yield (x, y)
        