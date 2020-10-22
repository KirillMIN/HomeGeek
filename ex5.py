class Stationery:

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки.')


class Pen(Stationery):
    @staticmethod
    def draw():
        print('Рисуем ручкой.')


class Pencil(Stationery):
    @staticmethod
    def draw():
        print('Рисуем карандашом.')


class Handle(Stationery):
    @staticmethod
    def draw():
        print('Рисуем маркером.')


work_book = Stationery('book')
work_book.draw()
grammar_book = Pen('book')
grammar_book.draw()
copy_book = Handle('book')
copy_book.draw()

