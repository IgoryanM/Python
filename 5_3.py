with open('5_3.txt', encoding='utf8') as f:
    salary = 0
    count = 0
    for line in f:
        if int((line.split()[1])) < 20000:
            print((line.split()[0]), '< 20000')
        salary = salary + int((line.split()[1]))
        count  += 1

    print('Средний доход:', int(salary / count))
