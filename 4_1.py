from sys import argv
    
name, price, hour, prem = argv
pr = int(price)
hr = int(hour)
pre = int(prem)

print(name, (pr*hr+pre))

