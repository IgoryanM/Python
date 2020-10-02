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
        
    def turn (self):
        random.shuffle(self.bag)
        return self.bag.pop()
       
    def start(self, human_card, pc_card):
        while self.bag != []:
                
            num = self.turn()
            
            print(f'Новый бочонок: {num} осталось {len(self.bag)}\n----Ваша карточка----\n{ human_card}\n---------------------\n-Карточка компьютера-\n{pc_card}\n---------------------')
            
            if human_card.win():
                print ('\n★★★Победил игрок★★★')
                break
            if pc_card.win():
                print ('\n★★★Победил компьютер★★★')
                break
            
            for line in pc_card.new_card:
            	 	if num in line:
             			line[line.index(num)]  = '•'
            			
            my_turn = input('\nЗачеркнуть цифру? (y/n) ')
            if my_turn == 'y':
            	selector = False
            	for line in human_card.new_card:
            		if num in line:
            			line[line.index(num)]  = '•'
            			selector = True
            	if selector == False:
            		   print ('Вы ошиблись\n---Игрок проиграл---')
            		   break
 			          
    	       
hm_card = LotoCard()
cpu_card = LotoCard()  	   	
st = Game()  	   	   	   	

st.start(hm_card, cpu_card)