

my_list = [1, 0, 2, 2, 3, 4, 3, 7]
new = [elem for elem in my_list if my_list.count(elem) == 1]
print(new)
