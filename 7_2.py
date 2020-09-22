from abc import abstractmethod, ABC

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def new_price(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def consumption_coat(self):
        print(f'Расход ткани на пальто {self.name} - {self.v // 6.5 + 0.5}')
        return (self.v // 6.5 + 0.5)

    @property
    def print_price(self):
        return f'Цена {self.name} - {self.price}'

    def new_price(self, price=2500):
        self.price = price

class Costume(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def consumption_costume(self):
        print(f'Расход ткани на костюм {self.name} - {2 * self.h + 0.3}')
        return (2 * self.h + 0.3)

    @property
    def print_price(self):
        return f'Цена {self.name} - {self.price}'

    def new_price(self, price=1500):
        self.price = price


new_costume = Costume('Armani', 100)
new_costume.new_price()
print(new_costume.print_price)

new_coat = Coat('Gucci', 200)
new_coat.new_price()
print(new_coat.print_price)

print(f'Полный расход ткани - {new_costume.consumption_costume() + new_coat.consumption_coat()}')

