# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они 
# разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух
# вбивает в программу с клавиатуры. 

# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  

def compare_count_syllable(text):
    rus_vowels = "ауоыиэяюёе"
    count_syllable = 0
    first = True
    count_first_syllable = 0
    for word in phrase.split(" "):
        count_syllable = len([item for item in word if item in rus_vowels])
        if first: 
            first = False
            count_first_syllable = count_syllable
        else:
            if count_first_syllable != count_syllable:
                return False
    return True

phrase = "пара-ра-рам рам-пам-папам па-ра-па-да"

print(phrase)
print("Парам пам-пам") if compare_count_syllable(phrase) else print("Пам парам")
