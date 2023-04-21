# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств.
import random

#first_count_elements = int(input('Введите количество элементов в 1 наборе '))
#second_count_elements = int(input('Введите количество элементов в 2 наборе '))
first_count_elements = 5
second_count_elements = 7


# first_set_elements = [random.randint(-10,10) for count in range(first_count_elements)]
# second_set_elements = [random.randint(-10,10) for count in range(second_count_elements)]

# print(f'Первый набор: { first_set_elements }')
# print(f'Второй набор: {second_set_elements}')

# first_set = set(first_set_elements)
# second_set = set(second_set_elements)
# print(f'Первый упорядоченный набор: { first_set }')
# print(f'Второй упорядоченный набор: { second_set }')
first_set = set([random.randint(-10,10) for count in range(first_count_elements)])
second_set = set([random.randint(-10,10) for count in range(second_count_elements)])

first_set_elements = sorted(first_set)
second_set_elements = sorted(second_set)

print(f'Первый упорядоченный набор: { first_set_elements }')
print(f'Второй упорядоченный набор:: {second_set_elements}')
