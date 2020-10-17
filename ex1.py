from sys import argv

file_name, worked_hour, rate, benefit = argv


def calculation():
    result = (int(worked_hour) * int(rate)) + int(benefit)
    print(f"Your pay is equal {result}")


print(calculation())
