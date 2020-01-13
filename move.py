class Move:
    def __init__(self, piece=None, start=(0,0), end=(0,0), enpassant=False):
        self.piece = piece
        self.start = start
        self.end = end

    def apply(self, node):
        startx, starty = self.start
        node.board[startx + starty * 8] = None
        endx, endy = self.end
        
        if enpassant:
            node.board[endx + starty*8] = None
            
        node.board[endx + endy * 8] = self.piece
        node.update_checks()

    

