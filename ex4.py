def power(x, y):
    if x < 0 or y > 0:
        return "You can do that"
    elif x == 0:
        return 0
    else:
        step = -1
        speed = x
        while step > y:
            step = step - 1
            # print("power:", step)
            x = x * speed
            # print("number:", x)
        return f"1 / {x}"


number1 = int(input("input x:"))
number2 = int(input("input y:"))
print("it is your power:", power(number1, number2))
