
#######result_choice_message = "Выбрано меню номер "

#######file_not_found = "Файл телефонного справочника не найден"




#------------func-------------
def menu1(filename):
    global phonebook
    
    with open(filename,'r', encoding='utf-8') as file:
        lines = file.readlines()

    for contact in lines:
        phonebook.append(contact.strip().split(':'))
    print(open_without_error)

def menu2(filename):
    global phonebook
    contact = ""

    for count in range(len(phonebook)):
            for record in phonebook[count]:
                contact = contact + record + ':'
            contact = contact[:-1] + '\n'

    with open(filename,'w', encoding='utf-8') as file:
        file.writelines(contact)

def menu3():
    count = 0
    for i in phonebook:
        
        for record in phonebook[count]:
            print(record, end = ' \t| ')
        print()
        count += 1
        
def menu4():
    global phonebook
    record = list()
    last_record = [str(len(phonebook) + 1)]
    name = [input(enter_FIO)]
    phone = [input(enter_pn)]
    rem = [input(enter_rem)]
    record = last_record + name + phone + rem
    phonebook.append(record)

def menu7():
    global phonebook
    record_delete = input("Введите номер записи для удаления: ")
    for count in range(len(phonebook)):
        if record_delete == phonebook[count][0]:
            print(delete_message, end = '')
            for record in phonebook[count]:
                print(f"  {record}", end = '')
            print()
            phonebook.pop(count)
            return
    print(reenter_num)


def menu6():
    global phonebook
    record_edit = input(edit_message)
    search_record = False
    count = 0

    for count in range(len(phonebook)):
        if record_edit == phonebook[count][0]:
            search_record = True
            print(editing, end = '')
            for record in phonebook[count]:
                print(f"  {record}", end = '')
            print()
            break
    if not search_record:
        print(reenter_edit)
        return
    while search_record:
        print(edit_menu)
        print(choice_message, end = ' ')
        choice_edit_menu = int(input())
        if choice_edit_menu == 1:
            new_record = input(enter_new_num)
            phonebook[count][0] = new_record
        
        elif choice_edit_menu == 2:
            new_record = input(enter_new_FIO)
            phonebook[count][1] = new_record

        elif choice_edit_menu == 3:
            new_record = input(enter_new_num)
            phonebook[count][2] = new_record
        
        elif choice_edit_menu == 4:
            new_record = input(enter_new_rem)
            phonebook[count][3] = new_record
        
        elif choice_edit_menu == 5:
            for record in phonebook[count]:
                print(f"  {record}", end = '')
            print()
        
        elif choice_edit_menu == 6:
            menu3()

        elif choice_edit_menu == 0:
            search_record = False
#-----------------------------


default_file_phonebook = "phonebook.txt"
###runit = True
phonebook = list()

while runit:
    print(main_menu)
    choice_menu = int(input(choice_message))
    print(f"Выбран пункт меню {choice_menu}")

    if choice_menu == 1:
        menu1(default_file_phonebook)

    elif choice_menu == 2:
        menu2(default_file_phonebook)
        

    elif choice_menu == 3:
        menu3()
    
    elif choice_menu == 4:
        menu4()

    elif choice_menu == 5:
        print(" menu = 5")

    elif choice_menu == 6:
        menu6()

    elif choice_menu == 7:
        menu7()

    elif choice_menu == 0:
        print(good_bye)
        runit = False

    
