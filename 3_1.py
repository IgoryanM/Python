def my_div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('На ноль делить нельзя, введите числа заново')

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

my_div(a, b)
