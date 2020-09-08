import math

def fact(n):
    for i in range(1, n):
        yield math.factorial(i)

for el in fact(10):
	print(el)
	
