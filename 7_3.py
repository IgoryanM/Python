class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells < other.cells:
            print('Cell_1 is not bigger than cell_2')
        else:
            return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(abs(self.cells / other.cells))

    def make_order(self):
        count = self.cells
        while count >= 5:
            if count == 5:
                print('*****', end='')
                break
            print('*****')
            count -= 5
        print('*' * count, end='')

cell_1 = Cell(18)
cell_2 = Cell(10)
cell_1.make_order()

