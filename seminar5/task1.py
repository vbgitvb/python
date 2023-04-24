# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# Пример:

# A = 3; B = 5 -> 243 (3⁵)

# A = 2; B = 3 -> 8 


base = int(input('Введите число, которое надо возвести в степень '))
degree = int(input(f'Введите степень в которую надо возвести число: '))

def exponentiation(number: int, stepen: int):
    if stepen == 0:
        return 1
    elif stepen == 1:
        return number
    else:
        return number * exponentiation(number, stepen - 1)



print(f'Число {base} в степени {degree} = {exponentiation(base, degree)}')
