def my_func(arg1, arg2, arg3):
    if (arg1 > arg2) and (arg2 > arg3):
        return arg1 + arg2
    elif (arg3 > arg2) and (arg2 > arg1):
        return arg2 + arg3
    else:
        return arg3 + arg1


number1 = int(input("input first number:"))
number2 = int(input("input second number:"))
number3 = int(input("input third number:"))
print("max sum:", my_func(number1, number2, number3))
