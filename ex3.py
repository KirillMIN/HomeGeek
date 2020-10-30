class IntNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
element = 0
while element != 3:
    my_list[element] = my_list.insert(element, int(input('input numbers: ')))
    element = element + 1
try:
    for elem in my_list:
        if type(elem) != int:
            raise IntNumbers("You don't input int number !")
except IntNumbers as err:
    print(err)
else:
    print(f"Your list: {my_list}")

