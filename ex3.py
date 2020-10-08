number = int(input("input number:"))
year_dict = dict(Winter=(1, 2, 12), Spring=(3, 4, 5), Summer=(6, 7, 8), Autumn=(9, 10, 11))
for key, (v1, v2, v3) in year_dict.items():
    if number == v1 or number == v2 or number == v3:
        print(key)
year_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
flag = False
for row in year_list:
    if flag:
        break
    for elem in range(len(row)):
        if year_list[0][elem] == number:
            print("Winter")
            flag = True
        elif year_list[1][elem] == number:
            print("Spring")
            flag = True
        elif year_list[2][elem] == number:
            print("Summer")
            flag = True
        elif year_list[3][elem] == number:
            print("Autumn")
            flag = True

#year_list.index(number)







