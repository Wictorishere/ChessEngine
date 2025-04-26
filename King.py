from PyQt5.QtGui import QPixmap
import os

class King:
    def __init__(self, isWhite, position):
        self.name = "King"
        self.isWhite = isWhite
        self.position = position
        self.isKilled = False
        img_path = os.path.join(os.path.dirname(__file__), "Media", "WKImage.png" if isWhite else "BKImage.png")
        self.image = QPixmap(img_path)
        self.hasmoved = False

    def move(self, position, board):
        row, col = position
        row1, col1 = self.position  
        self.position = position
        board[row1][col1] = 0
        board[row][col] = 1 if self.isWhite else -1
        self.hasmoved = True
            
         
    def canMove(self, position):
        row, col = position
        row1, col1 = self.position
        if(abs(row - row1) <= 1 and abs(col - col1) <= 1):
            return True
        elif(abs(col - col1) == 2 and row == row1):
            return True        
        
        return False
        
    def isValidMove(self, position, board):
        row, col = position
        row1, col1 = self.position
        if(self.isWhite):
            if(board[row][col] > 0):
                return False 

            if(col - col1 == 2 and (not row == row1 or self.hasmoved or not board[0][7] == 5)):
                return False
            elif(col1 - col == 2 and (not row == row1 or self.hasmoved or not board[0][0] == 5)):
                return False
        else:
            if(board[row][col] < 0):
                return False 
            
            if(col - col1 == 2 and (not row == row1 or self.hasmoved or not board[7][7] == -5)):
                return False
            elif(col1 - col == 2 and (not row == row1 or self.hasmoved or not board[7][0] == -5)):
                return False
            
        return True