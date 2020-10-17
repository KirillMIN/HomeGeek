
my_list = [3, 2, 9, 4, 2, 8, 12, 12, 15]
new_list = [elem for elem in my_list if my_list[my_list.index(elem)] > my_list[my_list.index(elem)-1]]
print(new_list)
