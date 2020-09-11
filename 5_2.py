with open('5_2.txt') as f:
    count_line = 0
    count_word = 0
    for st in f:
        count_line += 1
        count_word = len(st.split())
        print(f'Номер строки - {count_line}, слов в строке - {count_word}')


