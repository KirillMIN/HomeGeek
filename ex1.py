# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(arg1, arg2):
    if arg2 == 0:
        return "You cant do that"
    else:
        division_args = arg1 / arg2
        return division_args


number1 = int(input("Input arg1:"))
number2 = int(input("Input arg2:"))
print(division(number1, number2))
