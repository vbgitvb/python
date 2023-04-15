# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

size_array = int(input('Введите кол-во элементов в массиве '))
find_count_number = int(input('Введите число от 1 до 10, количество которого надо посчитать '))

count = 0
array = [random.randint(1, 10) for i in range(size_array)]
count = array.count(find_count_number)

if count:
    print(f'Число { find_count_number } встречается в списке { array } раз:  { count } ')
else:
    print(f'Числа { find_count_number } нет в списке { array }')
