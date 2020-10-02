import random
import  os


class LotoCard:
    def __init__(self):
        self.new_card = []
        for i in range(3):
            line = random.sample(range(1, 91), 5)
            line.sort()

            for i in range(0, 4):
                line.insert((random.randint(0, 5)), '-')

            self.new_card.append(line)

    def __str__(self):
        return ('\n'.join(' '.join([str(el) for el in line]) for line in self.new_card))

    def win(self):
        iswin = True
        for line in self.new_card:
            st_line = str(line)
            for el in st_line:
                if el.isdigit() == True:
                    iswin = False
        return iswin
        
        
class Game:
    def __init__(self):
        self.bag = [el for el in range(1, 91)]

    def turn(self):
        random.shuffle(self.bag)
        return self.bag.pop()

    def start(self, human_card, pc_card):
        while self.bag != []:
            os.system("clear")
            num = self.turn()

            print(
                f'Новый бочонок: {num} осталось {len(self.bag)}\n----Ваша карточка----\n{human_card}\n\n---------------------\n\n-Карточка компьютера-\n{pc_card}\n\n---------------------')

            if human_card.win():
                print('\n★★★Победил игрок★★★')
                break
            if pc_card.win():
                print('\n★★★Победил компьютер★★★')
                break

            for line in pc_card.new_card:
                if num in line:
                    line[line.index(num)] = '∅'

            my_turn = input('\nЗачеркнуть цифру? (y/n) ')
            while my_turn != 'y' and my_turn != 'n':
                print('Введите корректную команду')
                my_turn = input('\nЗачеркнуть цифру? (y/n) ')
            selector = False
            if my_turn == 'y':
                for line in human_card.new_card:
                    if num in line:
                        line[line.index(num)] = '∅'
                        selector = True
            if my_turn == 'n':
                for line in human_card.new_card:
                    if num not in line:
                        selector = True
                    else:
                        selector = False

            if selector == False:
                print('Вы ошиблись\n---Игрок проиграл---')
                break
            
        restart = input('\nИграть ещё? (y/n) ')
        while restart != 'y' and restart != 'n':
            print('Введите корректную команду')
            restart = input('\n Играть ещё? (y/n) ')
        if restart == 'y':
            self.__init__()
            self.start(LotoCard(), LotoCard())    
        if restart == 'n':
        	exit()
        	

hm_card = LotoCard()
cpu_card = LotoCard()
st = Game()

st.start(hm_card, cpu_card)