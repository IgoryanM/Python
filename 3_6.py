def int_func(text):
    
    list_cap = []
    list_text = str.split(text)
    
    for el in list_text:
        list_cap.append(str.capitalize(el))
    
    return(' '.join(list_cap))
    
print(int_func('python qwe asd zxc'))

