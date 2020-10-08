#change_list = [2, 'text', 456, 45.3, None, 5]
#change_list = [2, 'text', 456, 6, 7]
change_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(change_list)
for index in range(int(len(change_list) / 2)):
    change_list[2 * index], change_list[2 * index + 1] = change_list[2 * index + 1], change_list[2 * index]
print(change_list)
