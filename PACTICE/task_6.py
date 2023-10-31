# Вводятся два вещественных числа в одну строку через пробел. Вывести на экран наибольшее из чисел. Задачу решить
# с помощью условного оператора.

num_1 = float(input('Enter the number one: '))
num_2 = float(input('Enter the number two: '))

if num_1 > num_2:
    print(f"Наибольшее число: {num_1} ")
else:
    print(f"Наибольшее число: {num_2} ")

