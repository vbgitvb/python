# Task3. Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма 
# первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# Пример:

# 385916 -> yes

# 123456 -> no

num_bilet = input('Введите номер билета: ')
if num_bilet.isdigit:
    sum_left_digits = int(num_bilet[0]) + int(num_bilet[1]) + int(num_bilet[2])
    sum_right_digits = int(num_bilet[-1]) + int(num_bilet[-2]) + int(num_bilet[3])
    if sum_left_digits == sum_right_digits:
        print(f'Билет счастливый')
    else:
        print(f'Билет обычный')
else:
    print('Введено не число')

