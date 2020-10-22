class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self. _income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}, {self.position}')

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        return print(f'Your salary: {total_income}')


Ivan = Position("Ivan", 'Bubnov', "worker", 10000000, 500000)
Ivan.get_full_name()
Ivan.get_total_income()

