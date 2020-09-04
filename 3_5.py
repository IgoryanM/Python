my_sum = 0
esc = False

while True:
    sum_list = str.split(input('Enter number: '))
    
    for el in sum_list:
        if str.isdigit(el) == False:
            esc = True
            print(my_sum)  
            break
       
        my_sum = int(el) + my_sum
    
    if esc == True:
        break
        
    print(my_sum)   
     
    
