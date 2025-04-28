from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os

class Pawn:
    def __init__(self, isWhite, position):
        self.name = "Pawn"
        self.isWhite = isWhite
        self.position = position
        self.isKilled = False
        img_path = os.path.join(os.path.dirname(__file__), "Media", "WPImage1.png" if isWhite else "BPImage1.png")
        self.image = QPixmap(img_path).scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.hasMoved = False
        self.enpassant = False

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
                if(board[row][col] > 0):
                    return False
                elif (col1 - 1 == col):
                    if (board[row][col] == 0 and not board[row1][col1 - 1] == 6):
                        return False
                    elif board[row][col] == 0 and not board[row1][col1 - 1] == 6:
                        self.enpassant = True
                        return True
                elif (col1 + 1 == col):
                    if (board[row][col] == 0 and not board[row1][col1 + 1] == 6):
                        self.enpassant = True
                        return False
                    elif board[row][col] == 0 and not board[row1][col1 + 1] == 6:
                        self.enpassant = True
                        return True
            elif col == col1 and board[row][col1] != 0:
                return False

        else:
            if(board[row][col] < 0):
                return False 
            elif row == row1 - 1 and abs(col - col1) == 1: 
                if(board[row][col] < 0):
                    return False
                elif(col1 - 1 == col):
                    if (board[row][col] == 0 and not board[row1][col1 - 1] == 6):
                        self.enpassant = False
                        return True
                    elif board[row][col] == 0 and not board[row1][col1 - 1] == 6:
                        print("yes")
                        self.enpassant = True
                        return True
                elif(col1 + 1 == col):
                    if (board[row][col] == 0 and not board[row1][col1 + 1] == 6):
                        self.enpassant = False
                        print(board[row1][col1 + 1])
                        return True
                    elif board[row][col] == 0 and board[row1][col1 + 1] == 6:
                        self.enpassant = True
                        return True
            elif col == col1 and board[row][col1] != 0:
                return False
            
        
            
        return True
