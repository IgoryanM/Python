my_str = 'qwe asd 0123456789101112'

new_str = my_str.split(' ')

for i, el in enumerate(new_str, 1):
    if len(el) > 10:
        el = el[:10]
    print(i, el)