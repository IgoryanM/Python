class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print('Total_income -', (self._income['wage'] + self._income['bonus'] * self._income['wage'] * 0.01))

person = Position('Ivan', 'Ivanov', 'Python developer', 3000, 10)

person.get_full_name()
person.get_total_income()






