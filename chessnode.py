class ChessNode:
    def __init__(self, parent = None):
        self.list_of_moves = parent.list_of_moves.copy() if parent else []
        self.is_checkmate = False
        self.white_turn = True
        self.board = parent.board.copy() if parent else [None]*64
        self.blackControls = [False]*64
        self.whiteControls = [False]*64
        self.white_can_short_castle = parent.white_can_short_castle if parent else True
        self.white_can_long_castle = parent.white_can_long_castle if parent else True
        self.black_can_short_castle = parent.black_can_short_castle if parent else True
        self.black_can_long_castle = parent.black_can_long_castle if parent else True
        self.white_in_check = parent.white_in_check if parent else False
        self.black_in_check = parent.black_in_check if parent else False
        
    def print_board(self):
        b = self.board
        print("+---+---+---+---+---+---+---+---+")
        for i in range(0, 8):
            x = (7-i) * 8
            # print("|   |   |   |   |   |   |   |   |")
            print(f"| {b[x].notation if b[x] else ' '} | {b[x+1].notation if b[x+1] else ' '} | {b[x+2].notation if b[x+2] else ' '} | {b[x+3].notation if b[x+3] else ' '} | {b[x+4].notation if b[x+4] else ' '} | {b[x+5].notation if b[x+5] else ' '} | {b[x+6].notation if b[x+6] else ' '} | {b[x+7].notation if b[x+7] else ' '} | {8-i}")
            print("+---+---+---+---+---+---+---+---+")
        print("  A   B   C   D   E   F   G   H  ")
        
        print(f"{'White' if self.white_turn else 'Black'} to move")
    
    def static_evaluation(self, white):
        # This is where the magic happens
        self.white_turn = white
        if self.is_checkmate:
            return 2000000 * (-1 if self.white_turn else 1)
            
        return self.count_material_imbalance()
        
    def count_material_imbalance(self):
        total = 0
        for x in range(0,64):
            if (piece := self.board[x]) != None:
                total += piece.base_value() * (1 if piece.is_white else -1)
        
        return total

    def is_terminal_node(self):
        # Checkmate, Stalemate and Draw conditions
        #if len(list(self.children())) == 0:
        #    self.is_checkmate = True
        #    return True
            
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
                            
                    for sx,sy in piece.attacks(self):
                        if piece.is_white:
                            self.whiteControls[sx + sy * 8] = True
                        else:
                            self.blackControls[sx + sy * 8] = True
                            
        try:
            if self.whiteControls[self.blackKing.x + self.blackKing.y*8]:
                self.black_in_check = True
            if self.blackControls[self.whiteKing.x + self.whiteKing.y*8]:
                self.white_in_check = True
        except:
            self.print_board()

    def children(self, white):
        # Generates new board configurations
        self.white_turn = white
        for y in range(8):
            for x in range(8):
                piece = self.board[x+y*8]
                if piece is not None and piece.is_white == self.white_turn:
                    for move in piece.moves(self):
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
