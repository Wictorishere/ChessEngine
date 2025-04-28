import sys
from PyQt5.QtWidgets import QApplication
from board import ChessBoard

def main():
    app = QApplication(sys.argv)
    board = ChessBoard()
    board.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()