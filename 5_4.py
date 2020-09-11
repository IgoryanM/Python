ls = []
with open('5_4.txt', encoding='utf-8-sig') as f:
	
	for line in f:
		st = str.split(line)
		if st[0] == 'One':
			st[0] = 'Один'
		if st[0] == 'Two':
			st[0] = 'Два'
		if st[0] == 'Three':
			st[0] = 'Три'
		elif st[0] == 'Four':
			st[0] = 'Четыре'
		ls.append(' '.join(st) + '\n')
	
with open('new5_4.txt', 'a') as d:
		d.writelines(ls)
		
		