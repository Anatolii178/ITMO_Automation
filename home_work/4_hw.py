# 1. создайте класс прямоугольника.
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3.5, 8)
rect3 = Rectangle(2, 3)

print('Площадь rect1 =', rect1.square())
print('Периметр rect1 =', rect1.perimeter())

print('Площадь rect2 =', rect2.square())
print('Периметр rect2 =', rect2.perimeter())

print('Площадь rect3 =', rect3.square())
print('Периметр rect3 =', rect3.perimeter())

print('\n')

# 2. Создайте класс Math.
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


math = Math(10, 5)

print('Сложение -', math.addition())
print('Умножение -', math.multiplication())
print('Деление -', math.division())
print('Вычитание -', math.subtraction())

print('\n')

# 3. откройте страницу https://demoqa.com/text-box
class Button2Level:

    type: str = 'Кнопка'

    def __init__(self, text, loc=''):
        self.text = text
        self.link = loc

    def click(self):
        return f'Клик по кнопке {self.text}'

but1 = Button2Level('Text Box')
but2 = Button2Level('Check Box')
but3 = Button2Level('Radio Button')
but4 = Button2Level('Web Tables')
but5 = Button2Level('Buttons')
but6 = Button2Level('Links')
but7 = Button2Level('Broken Links - Images')
but8 = Button2Level('Upload and Download')
but9 = Button2Level('Dynamic Properties')

# print(home.text)
print('Кнопка ' + but1.text)
print('Кнопка ' + but2.text)
print('Кнопка ' + but3.text)
print('Кнопка ' + but4.text)
print('Кнопка ' + but5.text)
print('Кнопка ' + but6.text)
print('Кнопка ' + but7.text)
print('Кнопка ' + but8.text)
print('Кнопка ' + but9.text)

print('\n')

print(but1.click())
print(but2.click())
print(but3.click())
print(but4.click())
print(but5.click())
print(but6.click())
print(but7.click())
print(but8.click())
print(but9.click())


