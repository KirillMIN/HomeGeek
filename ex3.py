with open('file.txt', 'r') as my_file:
    salary = []
    poorest = []
    list = my_file.readlines()
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
            poorest.append(i[0])
        salary.append(i[1])
    print(f'Оклад меньше 20.000 {poorest}, средний оклад {sum(map(int, salary)) / len(salary)}')

