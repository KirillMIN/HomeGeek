class NumbersError:
    def __init__(self):
        self.my_list = []

    def list_input(self):
        while True:
            try:
                value = int(input('input values:'))
                self.my_list.append(value)
                print(f'list - {self.my_list}')
            except:
                print(f"You can't write str")
                yes_no = input(f'Do you want to write again? Y/N ')

                if yes_no == 'Y':
                    print(self.list_input())
                elif yes_no == 'N':
                    return f'end of try'
                else:
                    break


try_ex = NumbersError()
print(try_ex.list_input())

