def task_1(a: int = 5, b: float = 3.5, c: str = 'point', d: list = [1, 2], e: bool = True) -> None:
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))


task_1()

print('\n')

def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
    return a[0:3]


print(task_2())
# последовательность Фибоначчи

print('\n')

def task_3(a: int) -> int:   # можно еще  def task_3(a: float) -> float:
    return a ** 2


print(task_3(5))

