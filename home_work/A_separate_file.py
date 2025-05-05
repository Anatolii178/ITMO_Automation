
class Car:

    def __init__(self, color, type, year):
# def __init__(self, color: str, type: str, year: int):   ТАК МОЖНО??? и указать значение? year: int = 2022
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return 'Автомобиль заведен'

    def stop(self):
        return 'Автомобиль заглушен'

    def app_year(self):
        return f'Автомобиль {self.year} года выпуска'

    def app_type(self):
        return f'Автомобиль {self.type} типа'

    def app_color(self):
        return f'Автомобиль {self.color} цвета'


car = Car('синего', 'R', 2022)

print(car.start())
print(car.stop())
print(car.app_year())
print(car.app_type())
print(car.app_color())
