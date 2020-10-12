def my_sum():
    res_sum = 0
    func = 1
    while func != 0:
        number = input('Input numbers or Q for quit - ').split()
        res = 0
        for element in range(len(number)):
            if number[element] == 'q' or number[element] == 'Q':
                func = 0
                break
            else:
                res = res + int(number[element])
        res_sum = res_sum + res
        print(f'Current sum is {res_sum}')
    print(f' final sum is {res_sum}')


print(my_sum())
