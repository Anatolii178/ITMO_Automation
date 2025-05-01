# Программа проверяет является число положительным, равно 0
# или отрицательным и выводит соответствующее сообщение.

num_float = 3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


num_float = 0

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True  # False (Печать запрещена)
num = 5

if num > 0 and permit_print:   # or (num - положительное число), and (ничего)
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


def student(year):
    if 1 <= year <= 4:
        print('Бакалавр')
    elif year == 5 or year == 6:
        print('Магистр')
    elif 7 <= year <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')


student(4)


def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('Вы - бакалавр')
    elif year_of_study in range(5, 7):
        print('Вы - магистр')
    elif 7 <= year_of_study <= 9:
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')


student_rank(9)


def number(b):
    if b > 100 or b < -100:
        print('-')
    else:
        print('+')


number(-10)


a = 10

if a > 100 or a < -100:
    print('-')
else:
    print('+')