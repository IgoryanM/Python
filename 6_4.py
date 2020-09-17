class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('On going...')

    def stop(self):
        print('Stoped.')

    def turn(self, direction):
        print('Turnig to the', self.direction)

    def show_speed(self):
        print(self.name, self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости')

class PoliceCar(Car):
    pass

bmw = TownCar(70, 'white', 'i3', False )
audi = WorkCar(100, 'blue', 'A3', True)

print(bmw.color)
print(audi.is_police)

bmw.show_speed()
audi.show_speed()

