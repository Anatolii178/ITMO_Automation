# определяем функцию
def add(x, y):
    return x + y

# вызываем функцию
# add(1, 2)

print(add(1, 2))

# вызываем функцию с другими аргументами
print(add('I a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))
print(arg(2, 2))
print(arg(1, 1, 1))
# print(arg(1, 1, '1', 1)) числа истроки не складываются

print(arg('1', '1', '1', '1'))
print(arg(1, 1.5, 1, 1))

def range_arg(a, b, c, d):
    return a+ ' ' +b+ ' '+ c+ ' '+ d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))


def a(b=(1, 2, 3, 4)):
    return b[1]

print(a())

def c(radius, pi=3.14159):
    return pi * radius**2

print('S=', c(2))