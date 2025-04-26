import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QInputDialog
from King import King
from Queen import Queen
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Pawn import Pawn


class Square(QLabel):
    def __init__(self, color, row, col, parent=None):
        super().__init__(parent)
        self.color = color
        self.row = row
        self.col = col
        self.piece = None
        self.setFixedSize(100, 100)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: {};".format(self.color))
        self.moves = {}

    def setPiece(self, piece):
        self.piece = piece
        self.setPixmap(piece.image if piece else QPixmap())

    def clearPiece(self):
        self.piece = None
        self.clear()

class ChessBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Engine v1.0.0")
        self.setFixedSize(800, 800)
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.selected_square = None
        self.turn = True
        
        self.white_king = King(True, (0, 3))
        self.black_king = King(False, (7, 3))

        self.white_queen = Queen(True, (0, 4))
        self.black_queen = Queen(False, (7, 4))

        self.white_rook1 = Rook(True, (0, 0))
        self.white_rook2 = Rook(True, (0, 7))
        self.black_rook1 = Rook(False, (7, 0))
        self.black_rook2 = Rook(False, (7, 7))

        self.white_bishop1 = Bishop(True, (0, 2))
        self.white_bishop2 = Bishop(True, (0, 5))
        self.black_bishop1 = Bishop(False, (7, 2))
        self.black_bishop2 = Bishop(False, (7, 5))

        self.white_knight1 = Knight(True, (0, 1))
        self.white_knight2 = Knight(True, (0, 6))
        self.black_knight1 = Knight(False, (7, 1))
        self.black_knight2 = Knight(False, (7, 6))

        self.white_pawn1 = Pawn(True, (1, 0))
        self.white_pawn2 = Pawn(True, (1, 1))
        self.white_pawn3 = Pawn(True, (1, 2))
        self.white_pawn4 = Pawn(True, (1, 3))
        self.white_pawn5 = Pawn(True, (1, 4))
        self.white_pawn6 = Pawn(True, (1, 5))
        self.white_pawn7 = Pawn(True, (1, 6))
        self.white_pawn8 = Pawn(True, (1, 7))

        self.black_pawn1 = Pawn(False, (6, 0))
        self.black_pawn2 = Pawn(False, (6, 1))
        self.black_pawn3 = Pawn(False, (6, 2))
        self.black_pawn4 = Pawn(False, (6, 3))
        self.black_pawn5 = Pawn(False, (6, 4))
        self.black_pawn6 = Pawn(False, (6, 5))
        self.black_pawn7 = Pawn(False, (6, 6))
        self.black_pawn8 = Pawn(False, (6, 7))
        
        
        
        self.board = [
            [5,4,3,1,2,3,4,5],
            [6,6,6,6,6,6,6,6],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [-6,-6,-6,-6,-6,-6,-6,-6],
            [-5,-4,-3,-1,-2,-3,-4,-5]
        ]

    
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(0)
        self.setLayout(grid)

        for row in range(8):
            for col in range(8):
                color = "#EEEED2" if (row + col) % 2 == 0 else "#769656"
                square = Square(color, row, col, self)
                square.mousePressEvent = lambda event, r=row, c=col: self.onSquareClicked(r, c)
                self.squares[row][col] = square
                grid.addWidget(square, row, col)

        self.addPieces()

    def addPieces(self):

        self.squares[0][3].setPiece(self.white_king)
        self.squares[7][3].setPiece(self.black_king)
        self.squares[0][4].setPiece(self.white_queen)
        self.squares[7][4].setPiece(self.black_queen)

        self.squares[0][0].setPiece(self.white_rook1)
        self.squares[0][7].setPiece(self.white_rook2)
        self.squares[7][0].setPiece(self.black_rook1)
        self.squares[7][7].setPiece(self.black_rook2)

        self.squares[0][2].setPiece(self.white_bishop1)
        self.squares[0][5].setPiece(self.white_bishop2)
        self.squares[7][2].setPiece(self.black_bishop1)
        self.squares[7][5].setPiece(self.black_bishop2)

        self.squares[0][1].setPiece(self.white_knight1)
        self.squares[0][6].setPiece(self.white_knight2)
        self.squares[7][1].setPiece(self.black_knight1)
        self.squares[7][6].setPiece(self.black_knight2)

        self.squares[1][0].setPiece(self.white_pawn1)
        self.squares[1][1].setPiece(self.white_pawn2)
        self.squares[1][2].setPiece(self.white_pawn3)
        self.squares[1][3].setPiece(self.white_pawn4)
        self.squares[1][4].setPiece(self.white_pawn5)
        self.squares[1][5].setPiece(self.white_pawn6)
        self.squares[1][6].setPiece(self.white_pawn7)
        self.squares[1][7].setPiece(self.white_pawn8)

        self.squares[6][0].setPiece(self.black_pawn1)
        self.squares[6][1].setPiece(self.black_pawn2)
        self.squares[6][2].setPiece(self.black_pawn3)
        self.squares[6][3].setPiece(self.black_pawn4)
        self.squares[6][4].setPiece(self.black_pawn5)
        self.squares[6][5].setPiece(self.black_pawn6)
        self.squares[6][6].setPiece(self.black_pawn7)
        self.squares[6][7].setPiece(self.black_pawn8)

    def onSquareClicked(self, row, col):
        board = self.board
        square = self.squares[row][col]

        if self.selected_square:
            piece = self.selected_square.piece
            if piece and self.turn == piece.isWhite:
                origin = piece.position
                if piece.canMove((row, col)) and piece.isValidMove((row, col), board):
                    if self.castling(piece, self.board, piece.isWhite, (row, col)):
                        self.selected_square.clearPiece()
                        piece.move((row, col), board)
                        square.setPiece(piece)

                        if self.check(piece.isWhite):
                            square.setStyleSheet("background-color: #e63946;")
                            QTimer.singleShot(500, lambda: square.setStyleSheet(f"background-color: {square.color};"))
                            square.clearPiece()
                            piece.move(origin, board)
                            self.squares[origin[0]][origin[1]].setPiece(piece)
                            print("It's Check!")
                        else:
                            self.turn = not self.turn
                    else:
                        print("Castling Unavailable")
                else:
                    square.setStyleSheet("background-color: #e63946;")
                    QTimer.singleShot(500, lambda: square.setStyleSheet(f"background-color: {square.color};"))
                    print("Invalid Move")

            if piece.name == "Pawn" and (
                    (piece.isWhite and piece.position[0] == 7) or (not piece.isWhite and piece.position[0] == 0)):
                self.promotion(piece)

            self.selected_square.setStyleSheet(
                f"background-color: {self.selected_square.color};")
            self.selected_square = None

        else:
            if square.piece:
                self.selected_square = square
                square.setStyleSheet("background-color: #03ff6c;")

        if self.checkMate(True):
            print("Black Won")
        elif self.checkMate(False):
            print("White Won")

    def check(self, isWhite, kingpos = None):
        if kingpos == None:
            king_pos = self.white_king.position if isWhite else self.black_king.position
        else :
            king_pos = kingpos

        for row in range(8):
            for col in range(8):
                piece = self.squares[row][col].piece
                if piece and piece.isWhite != isWhite:
                    if piece.canMove(king_pos) and piece.isValidMove(king_pos, self.board):
                        return True  
        return False
    
    def checkMate(self, isWhite):
        if not self.check(isWhite):
            return False  

        for row in range(8):
            for col in range(8):
                piece = self.squares[row][col].piece
                if piece and piece.isWhite == isWhite:
                    origin = piece.position
                    for r in range(8):
                        for c in range(8):
                            if piece.canMove((r, c)) and piece.isValidMove((r, c), self.board):
                                target_piece = self.squares[r][c].piece

                                self.squares[row][col].clearPiece()
                                piece.move((r, c), self.board)
                                self.squares[r][c].setPiece(piece)

                                in_check = self.check(isWhite)

                                self.squares[r][c].clearPiece()
                                piece.move(origin, self.board)
                                self.squares[row][col].setPiece(piece)
                                if target_piece:
                                    self.squares[r][c].setPiece(target_piece)

                                if not in_check:
                                    return False  

        return True 

    def castling(self, piece, board, isWhite, position):
        if piece.name != "King" or abs(position[1] - piece.position[1]) != 2:
            return True  

        row, col = position
        row1, col1 = piece.position

        if isWhite:
            if col < col1:
                if not (board[row1][col1 - 1] == 0 and board[row1][col1 - 2] == 0):
                    return False
                if self.check(True, (row1, col1)) or self.check(True, (row1, col1 - 1)) or self.check(True, (row1, col1 - 2)):
                    return False
                if not (self.white_rook1.position == (0, 0) and not self.white_rook1.hasMoved):               
                    return False
                
                self.squares[0][0].clearPiece()
                self.white_rook1.move((0, 2), self.board)
                self.squares[0][2].setPiece(self.white_rook1)
                

            elif col > col1:
                if not (board[row1][col1 + 1] == 0 and board[row1][col1 + 2] == 0 and board[row1][col1+3] == 0):
                    return False
                if self.check(True, (row1, col1)) or self.check(True, (row1, col1 + 1)) or self.check(True, (row1, col1 + 2)):
                    return False
                if not (self.white_rook2.position == (0, 7) and not self.white_rook2.hasMoved):
                    return False
                
                self.squares[0][7].clearPiece()
                self.white_rook2.move((0, 4), self.board)
                self.squares[0][4].setPiece(self.white_rook2)

        else:
            if col < col1:
                if not (board[row1][col1 - 1] == 0 and board[row1][col1 - 2] == 0):
                    return False
                if self.check(False, (row1, col1)) or self.check(False, (row1, col1 - 1)) or self.check(False, (row1, col1 - 2)):
                    return False
                if not (self.black_rook1.position == (7, 0) and not self.black_rook1.hasMoved):
                    return False

                self.squares[7][0].clearPiece()
                self.black_rook1.move((7, 2),self.board)
                self.squares[7][2].setPiece(self.black_rook1)

            elif col > col1:
                if not (board[row1][col1 + 1] == 0 and board[row1][col1 + 2] == 0 and board[row1][col1 +3] == 0):
                    return False
                if self.check(False, (row1, col1)) or self.check(False, (row1, col1 + 1)) or self.check(False, (row1, col1 + 2)):
                    return False
                if not (self.black_rook2.position == (7, 7) and not self.black_rook2.hasMoved):
                    return False

                self.squares[7][7].clearPiece()
                self.black_rook2.move((7, 4),self.board)
                self.squares[7][4].setPiece(self.black_rook2)

        return True


               
                    
    def unpassant():
        pass

    def promotion(self, pawn):
        row, col = pawn.position
        self.squares[row][col].clearPiece()

        options = ["Queen", "Rook", "Bishop", "Knight"]
        piece_name, ok = QInputDialog.getItem(self, "Promotion", "Choose a piece:", options, 0, False)

        if ok and piece_name:
            if piece_name == "Queen":
                new_piece = Queen(pawn.isWhite, (row, col))
                self.board[row][col] = 2 if pawn.isWhite else -2
            elif piece_name == "Rook":
                new_piece = Rook(pawn.isWhite, (row, col))
                self.board[row][col] = 5 if pawn.isWhite else -5
            elif piece_name == "Bishop":
                new_piece = Bishop(pawn.isWhite, (row, col))
                self.board[row][col] = 3 if pawn.isWhite else -3
            elif piece_name == "Knight":
                new_piece = Knight(pawn.isWhite, (row, col))
                self.board[row][col] = 4 if pawn.isWhite else -4
            
            self.squares[row][col].setPiece(new_piece)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = ChessBoard()
    board.show()
    sys.exit(app.exec_())
