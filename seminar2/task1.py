# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
#повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

#head = орел = 1
#tail = решка = 0
import random
coins_number = int(input('Введите количество монет на столе '))
head = random.randint(1, coins_number)
tail = coins_number - head
print(f'На столе монет с орлом: { head } штук. Решкой вверх: { tail } штук')
if head > tail:
    print(f'Решек меньше. Нужно перевернуть решки орлом вверх в количестве { tail } штук')
else:
    print(f'Орлов меньше. Нужно перевернуть орлы решкой вверх в количестве { head } штук')
