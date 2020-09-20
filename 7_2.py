class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def consumption_coat(self):
        print(f'Расход ткани на пальто {self.name} - {self.v // 6.5 + 0.5}')
        return (self.v // 6.5 + 0.5)


class Costume(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def consumption_costume(self):
        print(f'Расход ткани на костюм {self.name} - {2 * self.h + 0.3}')
        return (2 * self.h + 0.3)


new_costume = Costume('Armani', 100)
new_coat = Coat('Gucci', 200)

#new_costume.consumption_costume()
#new_coat.consumption_coat()

print(f'Полный расход ткани - {new_costume.consumption_costume() + new_coat.consumption_coat()}')

