import time
import random


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
    	   print('Загрузка игры...', end='')  
    	   time.sleep(1)
    	   print('.', end='')
    	   time.sleep(1)
    	   print ('.')	   
    	   	   	   	
st = Game()  
st.start(1, 2)  	   	   	   	
d = LotoCard()
print(d)