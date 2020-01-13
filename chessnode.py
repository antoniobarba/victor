class ChessNode:
    def __init__(self, parent = None):
        self.white_turn = True
        self.board = parent.board if parent else [None]*64
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
        return False

    def update_checks(self):
        blackControls = [False]*64
        whiteControls = [False]*64
        whiteKing = None
        blackKing = None
        for x in range(8):
            for y in range(8):
                piece = self.board[x+y*8]
                if piece is not None:
                    if piece.is_king:
                        if piece.is_white:
                            whiteKing = piece
                        else:
                            blackKing = piece
                            
                    for move in piece.moves(node):
                        if piece.is_white:
                            whiteControls[piece.x + piece.y*8] = True
                        else
                            blackControls[piece.x + piece.y*8] = True
        if whiteControls[blackKing.x + blackKing.y*8]:
            self.black_in_check = True
        if blackControls[whiteKing.x + whiteKing.y*8]:
            self.white_in_check = True

    def children(self):
        # Generates new board configurations
        for x in range(8):
            for y in range(8):
                piece = self.board[x+y*8]
                if piece is not None:
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
