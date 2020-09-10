with open('5_1.txt', 'w') as f:
    while True:
        text = input('Inter your text: ')
        if text == '':
            break
        else:
            f.write(text)
