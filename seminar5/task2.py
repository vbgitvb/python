# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Пример:
# 2 2
# 4 

def sum(number_one: int, number_two: int):
    if number_two == 0:
        return number_one
    else:
        return sum(number_one + 1, number_two - 1)

number_first = int(input('Введите первое слагаемое: '))
number_second = int(input(f'Введите второе слагаемое: '))

print(f'{number_first} + {number_second} = {sum(number_first, number_second)}')
