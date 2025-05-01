def a(b=(1, 2, 3, 4)):
    return b[1]

print(a())
print(a((3, 5, 6, 9)))

def c(radius, pi=3.14159):
    return pi * radius**2

print('S=', c(2))


