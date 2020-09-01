my_list = []
new_list = []

while True:
    value = input('Enter some data or type esc for quit: ')
    if value == 'esc':
        break
    else:
        my_list.append(value)

print(my_list, '- your list')

if len(my_list) % 2 == 0:
    for i in range(0, len(my_list), 2):
        new_list.append(my_list[i + 1])
        new_list.append(my_list[i])

else:
    for i in range(0, len(my_list) - 1, 2):
        new_list.append(my_list[i + 1])
        new_list.append(my_list[i])
    new_list.append(my_list[len(my_list)-1])

print(new_list)
