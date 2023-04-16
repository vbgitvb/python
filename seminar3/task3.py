# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# *Пример:*
# ноутбук
#     12

lang = {
'eng' : {1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
           2 : ['D', 'G'],
           3 : ['B', 'C', 'M', 'P'],
           4 : ['F', 'H', 'V', 'W', 'Y'],
           5 : ['K'],
           8 : ['J', 'X'],
           10: ['Q', 'Z']
        },
'rus' : {1 : ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
           2 : ['Д', 'К', 'Л', 'М', 'П', 'У'],
           3 : ['Б', 'Г', 'Ё', 'Ь', 'Я'],
           4 : ['Й', 'Ы'],
           5 : ['Ж', 'З', 'Х', 'Ц', 'Ч'],
           8 : ['Ш', 'Э', 'Ю'],
           10: ['Ф', 'Щ', 'Ъ']
        }
}

text_lang = None
word = input('Введите слово на русском или английском языке: ')
word = word.upper()
compare_lang = lang.get('eng')
#for key, value in compare_lang.items():
for value in compare_lang.values():
     if word[0] in value:
         text_lang = 'eng'

if text_lang == None:
    compare_lang = lang.get('rus')
#    for key, value in compare_lang.items():
    for value in compare_lang.values():
        if word[0] in value:
            text_lang = 'rus'
if text_lang == None:
    print('Тест введен на непонятном языке. Повторите ввод на английском или русском.')
else:
    print(f'Язык текста: {text_lang}')
    compare_lang = lang.get(text_lang)
    summ = 0
    for get_char in word:
        for key, value in compare_lang.items():
            if get_char in value:
                summ += key
print(f'Количество очков: {summ}')



    