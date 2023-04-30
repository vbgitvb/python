# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше
# заданного максимума)

import random

n_element =  int(input('Введите сколько элементов списке, n: '))
first_element = int(input('Введите с какого элемента начать отображать список: '))
last_element = int(input('Введите каким элементом списка закончить отображать: '))

my_list = [random.randint(1,20) for _ in range(n_element)]
print(f'Список: {my_list}')
print(f'  Срез: {my_list[first_element:last_element+1]}') if last_element < n_element \
    else print(f'Номер последнего элемента лежит за пределами списка: {my_list[first_element:]}')





