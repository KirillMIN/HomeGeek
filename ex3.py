def my_func(arg1, arg2, arg3):
    if arg1 > arg2 and arg1 > arg3:
        return arg1
    elif arg2 > arg1 and arg2 > arg3:
        return arg2
    else:
        return arg3


number1 = int(input("input first number:"))
number2 = int(input("input second number:"))
number3 = int(input("input third number:"))
print("max number:", my_func(number1, number2, number3))
