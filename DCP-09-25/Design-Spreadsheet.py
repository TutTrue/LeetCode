class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}
        for c in string.ascii_uppercase:
            self.sheet[c] = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        col, row = self._getCell(cell)
        self.sheet[col][row] = value

    def resetCell(self, cell: str) -> None:
        col, row = self._getCell(cell)
        self.sheet[col][row] = 0

    def getValue(self, formula: str) -> int:
        left, right = formula.split("+")
        left = left[1:]
        return self._getValueOfCell(left) + self._getValueOfCell(right)

    def _getCell(self, cell: str):
        return cell[0], cell[1:]

    def _getValueOfCell(self, cell: str):
        if cell.isdigit():
            return int(cell)
        col, row = self._getCell(cell)
        return int(self.sheet[col][row])


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
