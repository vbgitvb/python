# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# Пример:
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

size_array = int(input('Введите кол-во элементов в массиве '))
find_diff_number = int(input('Введите число от 1 до 10, близкую величину которого надо найти '))

array = [random.randint(1, 10) for i in range(size_array)]
position = 0
min_difference = abs(find_diff_number - array[0])

print(f'Ищем близкое число к { find_diff_number } в списке { array }')
for i in range(1, len(array)):
    difference = abs(find_diff_number - array[i])
    if  difference < min_difference:
        min_difference = difference
        position = i

print(f'Близкое число к {find_diff_number} - это { array[position]}, { position } в списке, если считать с 0.')
