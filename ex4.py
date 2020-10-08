my_str1 = input("Введите строку:").split()
chars_per_line = 10
for index in range(len(my_str1)):
    if len(my_str1[index]) > 10:
        print(index+1, ")",  my_str1[index][0:10])
        continue
    print(index+1, ")", my_str1[index])

