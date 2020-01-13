class ChessNode:
    def __init__(self, parent = None):
        self.white_turn = True
        self.board = parent.board if parent else [None]*64
        self.blackControls = [False]*64
        self.whiteControls = [False]*64
        self.white_can_short_castle = parent.white_can_short_castle if parent else True
        self.white_can_long_castle = parent.white_can_long_castle if parent else True
        self.black_can_short_castle = parent.black_can_short_castle if parent else True
        self.black_can_long_castle = parent.black_can_long_castle if parent else True
        self.white_in_check = parent.white_in_check if parent else False
        self.black_in_check = parent.black_in_check if parent else False
        
    def static_evaluation(self):
        # This is where the magic happens
        return 0

    def is_terminal_node(self):
        # Checkmate, Stalemate and Draw conditions
        if len(self.children()) == 0:
            return True # This is checkmate // there must be a faster way to calculate checkmate
        return False

    def update_checks(self):
        self.whiteKing = None
        self.blackKing = None
        for x in range(8):
            for y in range(8):
                piece = self.board[x+y*8]
                if piece is not None:
                    if piece.is_king:
                        if piece.is_white:
                            self.whiteKing = piece
                        else:
                            self.blackKing = piece
                            
                    for move in piece.moves(node):
                        if piece.is_white:
                            self.whiteControls[piece.x + piece.y*8] = True
                        else
                            self.blackControls[piece.x + piece.y*8] = True
        if self.whiteControls[self.blackKing.x + self.blackKing.y*8]:
            self.black_in_check = True
        if self.blackControls[self.whiteKing.x + self.whiteKing.y*8]:
            self.white_in_check = True

    def children(self):
        # Generates new board configurations
        for x in range(8):
            for y in range(8):
                piece = self.board[x+y*8]
                if piece is not None and piece.is_white == self.white_turn:
                    for move in piece.moves(node):
                        child = ChessNode(self)
                        move.apply(child)
                        
                        # Checks
                        if self.white_turn:
                            if self.white_in_check and child.white_in_check:
                                # Illegal move: you must get out of check
                                continue
                            if not self.white_in_check and child.white_in_check:
                                # Illegal move: the piece is pinned
                                continue
                        else:
                            if self.black_in_check and child.black_in_check:
                                # Illegal move: you must get out of check
                                continue
                            if not self.black_in_check and child.black_in_check:
                                # Illegal move: the piece is pinned
                                continue
                            
                        yield child
