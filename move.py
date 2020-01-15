class Move:
    def __init__(self, piece=None, start=(0,0), end=(0,0), enpassant=False, long_castle=False, short_castle=False):
        self.piece = piece
        self.start = start
        self.end = end
        self.enpassant = enpassant
        self.short_castle = short_castle
        self.long_castle = long_castle

    def __str__(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        return f"{self.piece.notation}{letters[self.start[0]]}{self.start[1]}-{letters[self.end[0]]}{self.end[1]}"

    def apply(self, node):
        startx, starty = self.start
        node.board[startx + starty * 8] = None
        endx, endy = self.end
        
        if self.enpassant:
            node.board[endx + starty*8] = None # Remove the opponent's pawn enpassant
            
        if self.short_castle:
            rook = node.board[7 + endy * 8] # Move the king's rook
            node.board[7 + endy * 8] = None
            rook.not_moved_yet = False
            node.board[4 + endy * 8] = rook
            
        if self.long_castle:
            rook = node.board[0 + endy * 8] # Move the queen's rook
            node.board[0 + endy * 8] = None
            rook.not_moved_yet = False
            node.board[3 + endy * 8] = rook
            
        if self.short_castle or self.long_castle:
            if self.piece.is_white:
                node.white_can_short_castle = False
                node.white_can_long_castle = False
            else:
                node.black_can_short_castle = False
                node.black_can_long_castle = False
            
        node.board[endx + endy * 8] = self.piece
        self.piece.x = endx
        self.piece.y = endy
        node.list_of_moves.append(self)
        node.white_turn = not node.white_turn
        node.update_checks()

    

