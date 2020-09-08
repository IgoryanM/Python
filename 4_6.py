from itertools import count, cycle

def cou(start, stop):
	
	for i in count(start):
		if i == stop:
			break
		else:
			print(i)
			
cou(1, 100)

def cy(data, stop=5):
	
	i = 0
	for el in cycle(data):
		if i == stop:
			break
		else:
			print(el)
			i += 1
			
cy(['q', None, 1], 100)