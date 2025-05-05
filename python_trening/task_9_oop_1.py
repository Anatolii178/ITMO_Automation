from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc):
        self.loc = loc


search = Input('input#search')

print(search.loc)
print('\n')
print(search.check_text())
print('\n')


class Input(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Button(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Title(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Link(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


a = Input('a', '/a')
b = Button('b', '/b')
c = Title('c', '/c')
d = Link('d', '/d')

print(a.text)
print(a.loc)

print(b.text)
print(b.loc)

print(c.text)
print(c.loc)

print(d.text)
print(d.loc)

print('\n')

print(a.check_text())
print(b.check_text())
print(c.check_text())
print(d.check_text())
