
class NullDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


divider = int(input("input divider: "))
denominator = int(input("input denominator: "))

try:
    if denominator == 0:
        raise NullDivision("Your added 0!")
except NullDivision as err:
    print(err)
else:
    print(f"Your result: {divider / denominator}")



