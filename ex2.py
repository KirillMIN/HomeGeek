from abc import ABC, abstractmethod


class Textile(ABC):

    @abstractmethod
    def get_consumption(self):
        pass

    @abstractmethod
    def get_param(self):
        pass


class Coat(Textile):
    def __init__(self, coat_size):
        self.coat_size = coat_size

    @property
    def get_consumption(self):
        return f'расход на пальто: {self.coat_size / 6.5 + 0.5}'

    def get_param(self):
        return self.coat_size / 6.5 + 0.5


class Jacket(Textile):
    def __init__(self, jacket_size):
        self.jacket_size = jacket_size

    @property
    def get_consumption(self):
        return f'расход на костюм: {self.jacket_size * 2 + 0.3}'

    def get_param(self):
        return self.jacket_size * 2 + 0.3


coat = Coat(2)
jacket = Jacket(4)
print(coat.get_consumption)
print(jacket.get_consumption)
print(coat.get_param() + jacket.get_param())



