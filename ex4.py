class OfficeEquipmentWarehouse:
    def __init__(self, name, availability, price, quantity):
        self.quantity = quantity
        self.name = name
        self.availability = availability
        self.my_store = []
        self.price = price

    def transfer_from_warehouse(self, town):
        if self.availability:
            print(f" You can transfer {self.name} to {town} ")
        else:
            print('no  availability')

    def transfer_to_warehouse(self, quantities):
        try:
            if type(quantities) != int:
                print('You can not write str')
                raise ValueError
        except:
            print('stop')

        else:
            self.quantity += quantities
            print(f' quantity of {self.name}: {self.quantity}')

    def list_of_equipment(self):
        return {'Model': self.name,
                'Price': self.price,
                'Quantity': self.quantity,
                'Availability': self.availability}


class Equipment(OfficeEquipmentWarehouse):
    def __init__(self, size, price, name, availability, quantity):
        super().__init__(name, availability, price, quantity)
        self.size = size


class Printer(Equipment):
    def __init__(self, size, price, name, availability, quantity, paper):
        super().__init__(size, price, name, availability, quantity)
        self.paper = paper


class Copier(Equipment):
    def __init__(self, size, price, name, availability, quantity, ink):
        super().__init__(size, price, name, availability, quantity)
        self.ink = ink


class Scanner(Equipment):
    def __init__(self, size, price, name, availability, quantity, diodes):
        super().__init__(size, price, name, availability, quantity)
        self.diodes = diodes

    def list_of_equipment(self):
        return {'Model': self.name,
                'Price': self.price,
                'Quantity': self.quantity,
                'Availability': self.availability,
                'Diodes': self.diodes}


scanner = Scanner(10, 15000, 'Dron', True, 3, 2)
print(scanner.list_of_equipment())
#scanner.transfer_from_warehouse('Moscow')
#scanner.transfer_to_warehouse(5)
# print(scanner.my_unit)
#print(scanner.quantity)
#scanner.transfer_to_warehouse(5)
#print(scanner.list_of_equipment())
scanner.transfer_to_warehouse('gr')


