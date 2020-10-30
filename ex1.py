
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def get_int(cls, day_month_year):
        day_month_year = day_month_year.split('-')
        date = [int(elem) for elem in day_month_year]
        return date

    @staticmethod
    def get_valid(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 2020:
            return print("Right data")
        else:
            return print("Wrong data")


print(Data.get_int('12-01-2001'))
Data.get_valid(1, 2, 3)

