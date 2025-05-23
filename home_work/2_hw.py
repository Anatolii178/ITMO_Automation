# 3. задача 1
# a. создайте функцию task_1(), в теле функции:
# i. создайте 5 разных переменных с произвольным названием.
# ii. у каждой укажите тип, типы следующие
# 1. int, float, str, list, bool
# iii. заполните переменные произвольными значениями, с соответствующим для каждой типом
# iv. выведите тип данных каждой в консоль.
# b. в функцию добавьте аннотацию возвращаемых данных
# c. добавьте вызов функции.

def task_1(a: int = 5, b: float = 3.5, c: str = 'point', d: list = [1, 2], e: bool = True) -> None:
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))


task_1()

print('\n')

# 4. задача 2
# a. создайте функцию task_2(), в теле функции:
# i. есть список a = [1, 2, 3, 5, 8, 13, 21]
# ii. выведите в консоль первые 3 значения списка
# b. в функцию добавьте аннотацию возвращаемых данных
# c. добавьте вызов функции.
# d. * - скажите как называется эта последовательность чисел

def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
    return a[0:3]


print(task_2())
# последовательность Фибоначчи

print('\n')

# 5. задача 3
# a. напишите функцию task_3(), которая принимает число и возвращает квадрат этого числа.
# b. пропишите аннотации для функции и аргумента
# c. распечатайте в консоль вызов функции

def task_3(a: int) -> int:   # можно еще  def task_3(a: float) -> float:
    return a ** 2


print(task_3(5))

