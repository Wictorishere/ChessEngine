from PyQt5.QtGui import QPixmap
import os

class Pawn:
    def __init__(self, isWhite, position):
        self.name = "Pawn"
        self.isWhite = isWhite
        self.position = position
        self.isKilled = False
        img_path = os.path.join(os.path.dirname(__file__), "Media", "WPImage.png" if isWhite else "BPImage.png")
        self.image = QPixmap(img_path)
        self.hasMoved = False  

    def move(self, position, board):
        row, col = position
        row1, col1 = self.position
        
        self.position = position
        board[row1][col1] = 0
        board[row][col] = 6 if self.isWhite else -6
        self.hasMoved = True

    def canMove(self, position):
        row, col = position
        row1, col1 = self.position

        if self.isWhite:
            if row == row1 + 1 and col == col1:
                return True
            elif row == row1 + 2 and col == col1 and not self.hasMoved: 
                return True
            elif row == row1 + 1 and abs(col - col1) == 1: 
                return True
        else:
            if row == row1 - 1 and col == col1: 
                return True
            elif row == row1 - 2 and col == col1 and not self.hasMoved:  
                return True
            elif row == row1 - 1 and abs(col - col1) == 1:
                return True

        return False
    
    def isValidMove(self, position, board):
        row, col = position
        row1, col1 = self.position
        if(self.isWhite):
            if(board[row][col] > 0):
                return False 
            elif row == row1 + 1 and abs(col - col1) == 1: 
                if(board[row][col] >= 0):
                    return False
            elif col == col1 and board[row][col1] != 0:
                return False

        else:
            if(board[row][col] < 0):
                return False 
            elif row == row1 - 1 and abs(col - col1) == 1: 
                if(board[row][col] <= 0):
                    return False
            elif col == col1 and board[row][col1] != 0:
                return False
            
        
            
        return True
