from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


n = int(input("amount of numbers"))
x = 0
for i in fact():
    if x < n:
        print(n)
        x += 1
    else:
        break
