import alfabeta
from pawn import *
from bishop import *
from knight import *
from king import *
from queen import *
from rook import *
from chessnode import *

def setup_board():
    root = ChessNode()
    
    # Setup white pieces
    root.board[0 + 0] = Rook(0, 0)
    root.board[1 + 0] = Knight(1, 0)
    root.board[2 + 0] = Bishop(2, 0)
    root.board[3 + 0] = Queen(3, 0)
    root.board[4 + 0] = King(4, 0)
    root.board[5 + 0] = Bishop(5, 0)
    root.board[6 + 0] = Knight(6, 0)
    root.board[7 + 0] = Rook(7, 0)
    for x in range(0, 8):
        root.board[x + 8] = Pawn(x, 1)
        
    # Setup black pieces
    root.board[0 + 56] = Rook(0, 7, False)
    root.board[1 + 56] = Knight(1, 7, False)
    root.board[2 + 56] = Bishop(2, 7, False)
    root.board[3 + 56] = Queen(3, 7, False)
    root.board[4 + 56] = King(4, 7, False)
    root.board[5 + 56] = Bishop(5, 7, False)
    root.board[6 + 56] = Knight(6, 7, False)
    root.board[7 + 56] = Rook(7, 7, False)
    for x in range(0, 8):
        root.board[x + 48] = Pawn(x, 6, False)
        
    root.update_checks()
    return root
    
r = setup_board()
r.print_board()
score, moves = alfabeta.alfa_beta(r, 4, -1000000000, 1000000000, True)
print(f"score = {score}")
print(f"moves = {[m.__str__() for m in moves]}")
