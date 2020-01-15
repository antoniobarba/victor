from piece import Piece
from rook import Rook
from move import Move

class King(Piece):
    def __init__(self, x=0, y=0, is_white=True, not_moved_yet=True):
        super().__init__(x, y, is_white, is_king=True)
        self.not_moved_yet = not_moved_yet
        self.notation = "K" if is_white else "k"
		
    def base_value(self):
        return 1000000
    
    def moves(self, node):
        # Short Castle rules
        # if castling rights are set and the king as not moved yet
        if node.white_can_short_castle and self.is_white and self.not_moved_yet and not node.white_in_check:
            # if the king's rook is present and has not moved yet
            if (piece := node.board[7 + self.y*8]) != None and isinstance(piece, Rook) and piece.not_moved_yet and piece.is_white:
                # if the two squares to the right are free
                if node.board[5 + self.y * 8] == None and node.board[6 + self.y * 8] == None:
                    # ... and they are not in check by the opponent
                    if not node.blackControls[5 + self.y * 8] and not node.blackControls[6 + self.y * 8]:
                        yield Move(King(6,0, is_white=True, not_moved_yet=False), (self.x, self.y), (6,0), short_castle=True)
        
        # Long Castle rules
        # if castling rights are set and the king as not moved yet
        if node.white_can_long_castle and self.is_white and self.not_moved_yet and not node.white_in_check:
            # if the queens's rook is present and has not moved yet
            if (piece := node.board[0 + self.y*8]) != None and isinstance(piece, Rook) and piece.not_moved_yet and piece.is_white:
                # if the two squares to the left are free
                if node.board[2 + self.y * 8] == None and node.board[3 + self.y * 8] == None:
                    # ... and they are not in check by the opponent
                    if not node.blackControls[2 + self.y * 8] and not node.blackControls[3 + self.y * 8]:
                        yield Move(King(2,0, is_white=True, not_moved_yet=False), (self.x, self.y), (2,0), long_castle=True)
        
        # Short Castle black
        if node.black_can_short_castle and not self.is_white and self.not_moved_yet and not node.black_in_check:
            # if the king's rook is present and has not moved yet
            if (piece := node.board[7 + self.y*8]) != None and isinstance(piece, Rook) and piece.not_moved_yet and not piece.is_white:
                # if the two squares to the right are free
                if node.board[5 + self.y * 8] == None and node.board[6 + self.y * 8] == None:
                    # ... and they are not in check by the opponent
                    if not node.whiteControls[5 + self.y * 8] and not node.blackControls[6 + self.y * 8]:
                        yield Move(King(6,7, is_white=False, not_moved_yet=False), (self.x, self.y), (6,7), short_castle=True)
               
        # Long Castle black
        if node.black_can_long_castle and not self.is_white and self.not_moved_yet and not node.black_in_check:
            # if the king's rook is present and has not moved yet
            if (piece := node.board[0 + self.y*8]) != None and isinstance(piece, Rook) and piece.not_moved_yet and not piece.is_white:
                # if the two squares to the right are free
                if node.board[1 + self.y * 8] == None and node.board[2 + self.y * 8] == None:
                    # ... and they are not in check by the opponent
                    if not node.whiteControls[1 + self.y * 8] and not node.blackControls[2 + self.y * 8]:
                        yield Move(King(1,7, is_white=False, not_moved_yet=False), (self.x, self.y), (1,7), long_castle=True)    
                        
                
        
        x,y = self.x - 1, self.y - 1
        if x >= 0 and y >= 0:
            if self.is_white and not node.blackControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or not piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
            if not self.is_white and not node.whiteControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
        
        x,y = self.x - 1, self.y
        if x >= 0 and y >= 0:
            if self.is_white and not node.blackControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or not piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
            if not self.is_white and not node.whiteControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
        
        x,y = self.x - 1, self.y + 1
        if x >= 0 and y < 8:
            if self.is_white and not node.blackControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or not piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
            if not self.is_white and not node.whiteControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
        
        x,y = self.x, self.y - 1
        if y >= 0:
            if self.is_white and not node.blackControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or not piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
            if not self.is_white and not node.whiteControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
        
        x,y = self.x, self.y + 1
        if y < 8:
            if self.is_white and not node.blackControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or not piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
            if not self.is_white and not node.whiteControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
        
        x,y = self.x + 1, self.y - 1
        if x < 8 and y >= 0:
            if self.is_white and not node.blackControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or not piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
            if not self.is_white and not node.whiteControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
        
        x,y = self.x + 1, self.y
        if x < 8:
            if self.is_white and not node.blackControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or not piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
            if not self.is_white and not node.whiteControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
        
        x,y = self.x + 1, self.y + 1
        if x < 8 and y < 8:
            if self.is_white and not node.blackControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or not piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
            if not self.is_white and not node.whiteControls[x + y * 8] and ((piece := node.board[x + y*8]) == None or piece.is_white):
                yield Move(King(x, y, is_white = self.is_white), (self.x, self.y), (x,y))
        
    def attacks(self, node):
        x,y = self.x - 1, self.y - 1
        if x >= 0 and y >= 0:
            yield (x,y)
            
        x,y = self.x - 1, self.y
        if x >= 0 and y >= 0:
            yield (x,y)
        
        x,y = self.x - 1, self.y + 1
        if x >= 0 and y < 8:
            yield (x,y)
        
        x,y = self.x, self.y - 1
        if y >= 0:
            yield (x,y)
        
        x,y = self.x, self.y + 1
        if y < 8:
            yield (x,y)
        
        x,y = self.x + 1, self.y - 1
        if x < 8 and y >= 0:
            yield (x,y)
        
        x,y = self.x + 1, self.y
        if x < 8:
            yield (x,y)
        
        x,y = self.x + 1, self.y + 1
        if x < 8 and y < 8:
            yield (x,y)
            
        