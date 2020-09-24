import random
import os


class LotoCard:
    def __init__(self):	
        self.new_card = []

        for i in range(3):
            line = random.sample(range(1, 91), 5)
            line.sort()

            for i in range (0, 4):
                line.insert((random.randint(0, 5)), '-')
 
            self.new_card.append(line)

    def __str__(self):
    	return ('\n'.join(' '.join([str(el) for el in line]) for line in self.new_card))
    	
 
class Game:
    def __init__(self):
        self.bag = [el for el in range(1, 91)]
    
    def start(self, human_card, pc_card):
        
        #while self.bag != []:
            print(f'Новый бочонок: {self.turn()} осталось {len(self.bag)}')	  
            print(f'----Ваша карточка----\n{human_card}')
            print('---------------------')
            print(f'-Карточка компьютера-\n{pc_card}')
            print('---------------------')
            
            
           # os.system('clr') 
    		     
    def turn (self):
        random.shuffle(self.bag)
        return self.bag.pop()
        
    	       
human_card = LotoCard()
pc_card = LotoCard()	   	   	   	
st = Game()  	   	   	   	

st.start(human_card, pc_card)