class Soda:

    def __init__(self, add=None):
    # def __init__(self, add):
        self.add = add

    def show_my_drink(self):
        if self.add:
            # print('Газировка и {}'.format(self.add))
            print(f'Газировка и {self.add}')
            # return f'Газировка и {self.add}'
        else:
            print('Обычная газировка')
            # return 'Обычная газировка'


drink = Soda()
# drink = Soda('')
drinkplus = Soda('Добавка')

drink.show_my_drink()
drinkplus.show_my_drink()
# print(drink.show_my_drink())
# print(drinkplus.show_my_drink())