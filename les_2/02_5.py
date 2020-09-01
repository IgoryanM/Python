my_list = [7, 5, 3, 3, 2]
new_el = int(input('Enter your score: '))

if new_el in my_list:
    pos = my_list.index(new_el)
    count = my_list.count(new_el)
    my_list.insert(pos+count, new_el)

elif new_el > my_list[0]:
    my_list.insert(0, new_el)

else:
    my_list.append(new_el)

print(my_list)
