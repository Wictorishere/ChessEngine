class Move:
    def __init__(self, pieceName, take, row, col, Drow, Dcol, pieceTaken=None):
        self.pieceName = pieceName
        self.take = take
        self.row = row
        self.col = col
        self.Drow = Drow
        self.Dcol = Dcol
        self.pieceTaken = pieceTaken

    def __str__(self):
        if self.take:
            if self.pieceName == "Pawn":
                return f"{self.coltoabc(self.col)}x{self.coltoabc(self.Dcol)}{self.Drow + 1}"
            else:
                return f"{self.pieceName}x{self.coltoabc(self.Dcol)}{self.Drow + 1}"
        else:
            return f"{self.pieceName if self.pieceName != "Pawn" else ""}{self.coltoabc(self.Dcol)}{self.Drow + 1}"

    @staticmethod
    def coltoabc(col):
        match col:
            case 0: return 'A'
            case 1: return 'B'
            case 2: return 'C'
            case 3: return 'D'
            case 4: return 'E'
            case 5: return 'F'
            case 6: return 'G'
            case 7: return 'H'
