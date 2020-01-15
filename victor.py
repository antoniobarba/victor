import alfabeta
from pawn import *
from bishop import *
from knight import *
from king import *
from queen import *
from rook import *
from chessnode import *
from move import *

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
# score, moves = alfabeta.alfa_beta(r, 4, -1000000000, 1000000000, True)
# print(f"score = {score}")
#print(f"moves = {[m.__str__() for m in moves]}")
print('Enter "h" for help')
while (a := input('Move or "q" to quit: ')) != 'q':
    if a == 'h':
        print("'h' displays this screen")
        print("'q' quits to the command line")
        print("Moves are expressed in the form xNyM where x and y are the files whereas N and M are the ranks:")
        print("Examples: to move the Pawn d2 to d4 enter d2d4")
        print("To move the Knight b1 to c3 enter b1c3")
    else:
        # Convert command into a move object
        startCol, startRow, endCol, endRow = a
        columns = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        startX = columns[startCol]
        startY = int(startRow) - 1
        endX = columns[endCol]
        endY = int(endRow) - 1

        piece = r.board[startX + startY * 8]
        move = Move(piece, (startX, startY), (endX, endY))
        move.apply(r)
        r.list_of_moves.clear()
        r.print_board()

        score, moves = alfabeta.alfa_beta(r, 4, -1000000000, 1000000000, False)
        moves[0].apply(r)
        r.print_board()
        print(f"Score: {score}, variation: {[m.__str__() for m in moves]}")

