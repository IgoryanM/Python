import random
import os


class LotoCard:
    def __init__(self, name):	
        self.new_card = []
        self.name = name
        for i in range(3):
            line = random.sample(range(1, 91), 5)
            line.sort()

            for i in range (0, 4):
                line.insert((random.randint(0, 5)), '-')
 
            self.new_card.append(line)

    def __str__(self):
    	return ('\n'.join(' '.join([str(el) for el in line]) for line in self.new_card))
    	
    def win(self):
        iswin = True
        for line in self.new_card:
    	    line = str(line)
    	    for el in line:
    		    if el.isdigit() == False:
    			    iswin = False
        if iswin == True:
            print (f'Победил {self.name}')
           
 
class Game:
    def __init__(self):
        self.bag = [el for el in range(1, 91)]
    
    def start(self, human_card, pc_card):
        while self.bag != []:
            num = self.turn()
            print(f'Новый бочонок: {num} осталось {len(self.bag)}')	  
            print(f'----Ваша карточка----\n{human_card}')
            print('---------------------')
            print(f'-Карточка компьютера-\n{pc_card}')
            print('---------------------')         
            my_turn = input('\nЗачеркнуть цифру? (y/n) ')
            if my_turn == 'y':
            	selector = False
            	for line in human_card.new_card:
            		if num in line:
            			line[line.index(num)]  = '•'
            			selector = True
            	if selector == False:
            		   print ('---Игрок проиграл---')
            		   break
            	
            for line in pc_card.new_card:
            		if num in line:
            			line[line.index(num)]  = '•'
            			
            human_card.win()
            pc_card.win()
    		     
    def turn (self):
        random.shuffle(self.bag)
        return self.bag.pop()
        
    	       
hm_card = LotoCard('Player')
cpu_card = LotoCard('Computer')	   	   	   	
st = Game()  	   	   	   	

st.start(hm_card, cpu_card)