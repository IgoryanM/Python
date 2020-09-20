class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    def consumption_coat(self):
        print(f'Расход ткани на {self.name} - {self.v / 6.5 + 0.5}')


class Costume(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    def consumption_costume(self):
        print(f'Расход ткани на {self.name} - {2 * self.h + 0.3}')

new_costume = Costume('q', 1)
