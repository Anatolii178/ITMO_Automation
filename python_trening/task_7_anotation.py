# a: int = 5
# b: str = 'строка'
# c: list = [1, 2]
#
#
def indent(s:str, width:int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('123', 69))


# def fds(s:str = '') -> int:
#     return len(s)
#
# print(fds())
#
# def twolist(a:list, b:list) -> int:
#     return max(len(a), len(b))
#
# print(twolist([1], [1, 2]))

def addlist(a:list):
    a.append(6)
    return a

print(addlist(['один', 2, 3]))


def sumlist(a:list) -> int:
    b=0
    for elem in a:
        b= b + elem
    return b

print(sumlist([1,2,3]))



