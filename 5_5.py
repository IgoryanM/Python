with open('5_5.txt', 'w+') as f:
	f.write(input('Entrer numbers: '))
	f.seek(0)
	sm = sum(map(int, str.split((f.read()))))
	
	print(sm)
	
