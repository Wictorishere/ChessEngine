from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os

class Knight:
    def __init__(self, isWhite, position):
        self.name = "Knight"
        self.isWhite = isWhite
        self.position = position
        self.isKilled = False
        img_path = os.path.join(os.path.dirname(__file__), "Media", "WHImage1.png" if isWhite else "BHImage1.png")
        self.image = QPixmap(img_path).scaled(90, 90, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def move(self, position, board):
        row, col = position
        row1, col1 = self.position
        
        self.position = position
        board[row1][col1] = 0
        board[row][col] = 4 if self.isWhite else -4

    def canMove(self, position):
        row, col = position
        row1, col1 = self.position
        if (abs(row - row1) == 2 and abs(col - col1) == 1) or (abs(row - row1) == 1 and abs(col - col1) == 2):
            return True
        return False
    
    def isValidMove(self, position, board):
        row, col = position
        if(self.isWhite):
            if(board[row][col] > 0):
                return False 
        else:
            if(board[row][col] < 0):
                return False 
            
        return True
