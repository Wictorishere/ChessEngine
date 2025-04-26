from PyQt5.QtGui import QPixmap
import os

class Queen:
    def __init__(self, isWhite, position):
        self.name = "Queen"
        self.isWhite = isWhite
        self.position = position
        self.isKilled = False
        img_path = os.path.join(os.path.dirname(__file__), "Media", "WQImage.png" if isWhite else "BQImage.png")
        self.image = QPixmap(img_path)

    def move(self, position, board):
        row, col = position
        row1, col1 = self.position
        
        self.position = position
        board[row1][col1] = 0
        board[row][col] = 2 if self.isWhite else -2

    def canMove(self, position):
        row, col = position
        row1, col1 = self.position
        if(row == row1 or col == col1 or abs(row - row1) == abs(col - col1)):
            return True
        return False
    
    def isValidMove(self, position, board):
        row, col = position
        row1, col1 = self.position
        if self.isWhite:
            if board[row][col] > 0: 
                return False
        else:
            if board[row][col] < 0:
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
        elif abs(row - row1) == abs(col - col1):
            row_step = 1 if row > row1 else -1
            col_step = 1 if col > col1 else -1
            r, c = row1 + row_step, col1 + col_step
            while r != row and c != col:
                if board[r][c] != 0: 
                    return False
                r += row_step
                c += col_step

        return True
