from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os

class Bishop:
    def __init__(self, isWhite, position):
        self.name = "Bishop"
        self.isWhite = isWhite
        self.position = position
        self.isKilled = False
        img_path = os.path.join(os.path.dirname(__file__), "Media", "WBImage1.png" if isWhite else "BBImage1.png")
        self.image = QPixmap(img_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def move(self, position, board):
        row, col = position
        row1, col1 = self.position
        
        self.position = position
        board[row1][col1] = 0
        board[row][col] = 3 if self.isWhite else -3

    def canMove(self, position):
        row, col = position
        row1, col1 = self.position
        if(abs(row - row1) == abs(col - col1)):
            return True
        return False
    
    def isValidMove(self, position, board):
        row, col = position
        row1, col1 = self.position
        if(self.isWhite):
            if(board[row][col] > 0):
                return False 
        else:
            if(board[row][col] < 0):
                return False 
            

        row_step = 1 if row > row1 else -1
        col_step = 1 if col > col1 else -1
        r, c = row1 + row_step, col1 + col_step
        while r != row and c != col:
            if board[r][c] != 0: 
                return False
            r += row_step
            c += col_step

            
        return True
