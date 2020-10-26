
class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'Результат: {self.quantity * "*"}'

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) >= 0 else print('Отрицательно')

    def __mul__(self, other):
        return int(self.quantity * other.quantity)

    def __truediv__(self, other):
        return round(self.quantity // other.quantity)

    def make_order(self, cells_row):
        row = ''
        for i in range(int(self.quantity / cells_row)):
            row += f'{"*" * cells_row} \n'
        row += f'{"*" * (self.quantity % cells_row)}'
        return print(row)


cells_1 = Cell(10)
cells_2 = Cell(5)
print(cells_1)
print(cells_1)
print(cells_1 + cells_2)
print(cells_2 - cells_1)
print(cells_1 * cells_2)
# print(cells_1 / cells_2)
cells_1.make_order(2)

