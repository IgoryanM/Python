import json

avr = []
allfirm = {}
average_profit = {}

with open('5_7.txt') as f:
	for line in f:
		firm = str.split(line)
		earn = int(firm[2]) - int(firm[3])
		
		upd = {firm[0] : earn}
		allfirm.update(upd)
		
		if earn > 0:
		    avr.append(earn)

average_profit.update({'average_profit' : int(sum(avr)/len(avr))})	

firm_list = [allfirm, average_profit]

with open('5_7.json', 'w') as f:
	json.dump(firm_list, f)

		
		
		
		
		