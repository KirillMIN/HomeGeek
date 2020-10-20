rus_language = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file.txt', 'r') as file_obj1:
    for i in file_obj1:
        i = i.split()
        new_file.append(rus_language[i[0]] + ' - ' + i[2])
    print(new_file)

with open('file_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
