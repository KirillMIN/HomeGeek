class ComplexNumber:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def __add__(self, other):
        print(f'Sum of number1 and number2:')
        return f'Sum = {self.first_number + other.first_number} + {self.second_number + other.second_number} * i'

    def __mul__(self, other):
        print(f'Composition of number1 and number2:')
        return f'Comp = {self.first_number * other.first_number - (self.second_number * other.second_number)} + {self.second_number * other.first_number} * i'

    def __str__(self):
        return f's = {self.first_number} + {self.first_number} * i'


f_number1 = ComplexNumber(3, 7)
f_number2 = ComplexNumber(3, -2)
print(f_number1)
print(f_number1 + f_number1)
print(f_number1 * f_number1)
