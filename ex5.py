from functools import reduce


print(f'Список четных значений: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(lambda f_el,s_el: f_el * s_el, [el for el in range(99, 1001) if el % 2 == 0])}')
