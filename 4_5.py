from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]

def red(f_el, s_el):
    return f_el * s_el
    
print(reduce (red, my_list))