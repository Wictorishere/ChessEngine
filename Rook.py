from PyQt5.QtGui import QPixmap
import os

class Rook:
    def __init__(self, isWhite, position):
        self.name = "Rook"
        self.isWhite = isWhite
        self.position = position
        self.isKilled = False
        img_path = os.path.join(os.path.dirname(__file__), "Media", "WRImage.png" if isWhite else "BRImage.png")
        self.image = QPixmap(img_path)
        self.hasMoved = False

    def move(self, position, board):
        row, col = position
        row1, col1 = self.position
        
        self.position = position
        board[row1][col1] = 0
        board[row][col] = 5 if self.isWhite else -5
        self.hasMoved = True

    def canMove(self, position):
        row, col = position
        row1, col1 = self.position
        if(row == row1 or col == col1):
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
            
        if row == row1:
            step = 1 if col > col1 else -1
            for c in range(col1 + step, col, step):
                if board[row][c] != 0:  
                    return False
        elif col == col1:
            step = 1 if row > row1 else -1
            for r in range(row1 + step, row, step):
                if board[r][col] != 0: 
                    return False
            
        return True
