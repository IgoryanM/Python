my_month = int(input('Enter a month from 1 to 12: '))

#list

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]

if my_month in winter:
    print('It`s winter')
elif my_month in spring:
    print('It`s spring')
elif my_month in summer:
    print('It`s summer')
elif my_month in fall:
    print('It`s fall')

#dict

calend = {'winter':(12, 1, 2), 'spring':(3, 4, 5), 'summer':(6, 7, 8), 'fall':(9, 10, 11)}

for key, value in calend.items():
    if my_month in value:
        print('It`s ' + key)


