from itertools import count
from itertools import cycle


def count_func(start_number, stop_number):
    for elem in count(start_number):
        if elem > stop_number:
            break
        else:
            print(elem)


def cycle_func(my_list, iteration):
    i = 0
    it = cycle(my_list)
    while i < iteration:
        print(next(it))
        i += 1


count_func(start_number=int(input("enter start number: ")), stop_number=int(input("enter stop number: ")))
cycle_func(my_list=[1, 2], iteration=int(input("enter iteration: ")))
