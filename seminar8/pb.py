
main_menu = ''' \nГлавное меню
    1. Открыть телефонную книгу
    2. Сохранить телефонную книгу
    3. Показать контакты
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n '''

choice_message = "Выберете пункт меню: "
result_choice_message = "Выбран пункт меню: "
open_without_error = "Телефонный справочник успешно открыт"
file_not_found = "Файл телефонного справочника не найден"

#------------func-------------
def menu1(filename):
    global phonebook
    
    with open(filename,'r', encoding='utf-8') as file:
        lines = file.readlines()
        result = True
    for contact in lines:
        phonebook.append(contact.strip().split(':'))
    print(open_without_error)


def menu3():
    count = 0
    for i in phonebook:
        count += 1
        #print(f"{count}) {phonebook[count-1]}")
        print(f"{count}) {phonebook[count-1][1]} \t {phonebook[count-1][2]}\t {phonebook[count-1][3]}")
        #for info in phonebook[count-1]:
        #    print(f"info.")



#-----------------------------




default_file_phonebook = "phonebook.txt"
runit = True
phonebook = list()







while runit:
    print(main_menu)
    choice_menu = int(input(choice_message))

    if choice_menu == 1:
        menu1(default_file_phonebook)

    elif choice_menu == 2:
        print(" menu = 2")
        

    elif choice_menu == 3:
        print(" menu = 3")
        menu3()
    
    elif choice_menu == 3:
        print(" menu = 3")

    elif choice_menu == 4:
        print(" menu = 4")

    elif choice_menu == 5:
        print(" menu = 5")

    elif choice_menu == 6:
        print(" menu = 6")

    elif choice_menu == 7:
        print(" menu = 7")

    elif choice_menu == 8:
        print(" Завершаем работу.")
        runit = False

    
