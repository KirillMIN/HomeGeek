# change_list = [2, 'text', 456, 45.3, None, 5]
# change_list = [2, 'text', 456, 6, 7]
change_list = []
number = int(input("Введите конечное число элементов:"))
for index in range(number):
    new_element = input()
    change_list.append(new_element)
print(change_list)
for index in range(int(len(change_list) / 2)):
    change_list[2 * index], change_list[2 * index + 1] = change_list[2 * index + 1], change_list[2 * index]
print(change_list)
