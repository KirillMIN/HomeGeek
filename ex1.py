my_file = open('test.txt', 'w')
write_line = input('Введите текст:\n')
while write_line:
    my_file.writelines(write_line)
    write_line = input('Введите текст:\n')
    if not write_line:
        break

my_file.close()
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
