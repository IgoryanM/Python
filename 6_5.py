class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(self.title, 'Запуск отрисовки.')

class Pencil(Stationery):
    def draw(self):
        print(self.title, 'Запуск отрисовки.')

class Handle(Stationery):
    def draw(self):
        print(self.title, 'Запуск отрисовки.')

pen = Pen('1_pen')
pencil = Pencil('1_pencil')
handle = Handle('1_handle')

pen.draw()
pencil.draw()
handle.draw()