from text import *

list_menu_item = (1, 2, 3, 4, 5, 6, 7, 8, 0)
default_name_pb = "phonebook.txt"

def print_message(msg):
    print('\n' + '-' * len(msg) + '\n')
    print(msg)
    print('\n' + '=' * len(msg))


def print_main_menu():
    print(main_menu)

def select_item():
    while True:
        choice = int(input(choice_message))
        if choice in list_menu_item:
            return choice
        else:
            print_message(choice_not_existing_item)

def set_filename():
    name_pb_file = input(enter_name_file_pb)
    if len(name_pb_file) == 0:
        return default_name_pb
    return name_pb_file

def print_pb(book):
     count = 0
     for i in book:
         for record in book[count]:
             print(record, end = ' \t| ')
         print()
         count += 1

def enter_new_contact():
    record = list()
    #last_record = [str(len(book) + 1)]
    name = [input(enter_FIO)]
    phone = [input(enter_pn)]
    rem = [input(enter_rem)]
    record = name + phone + rem
    return record



def get_num_contact(msg: str):
    return int(input(msg))-1

def choice_item_edit(contact: list()):
    search_record = True
    while search_record:
        print(edit_menu)
        print(choice_message, end = ' ')
        choice_edit_menu = int(input())
        if choice_edit_menu == 1:
            contact[0] = input(enter_new_num)
        
        elif choice_edit_menu == 2:
            contact[1] = input(enter_new_FIO)

        elif choice_edit_menu == 3:
            contact[2] = input(enter_new_num)
        
        elif choice_edit_menu == 4:
            contact[3] = input(enter_new_rem)
        
        elif choice_edit_menu == 5:
            for record in contact:
                print(f"  {record}", end = '')
            print()

        elif choice_edit_menu == 0:
            search_record = False

    return contact

#------------------------------------------

# def edit_contact(book):
#     record_edit = input(edit_message)
#     search_record = False
#     count = 0

#     for count in range(len(book)):
#         if record_edit == book[count][0]:
#             search_record = True
#             print(editing, end = '')
#             for record in book[count]:
#                 print(f"  {record}", end = '')
#             print()
#             break
#     if not search_record:
#         print(reenter_edit)
#         return
#     while search_record:
#         print(edit_menu)
#         print(choice_message, end = ' ')
#         choice_edit_menu = int(input())
#         if choice_edit_menu == 1:
#             new_record = input(enter_new_num)
#             book[count][0] = new_record
        
#         elif choice_edit_menu == 2:
#             new_record = input(enter_new_FIO)
#             book[count][1] = new_record

#         elif choice_edit_menu == 3:
#             new_record = input(enter_new_num)
#             book[count][2] = new_record
        
#         elif choice_edit_menu == 4:
#             new_record = input(enter_new_rem)
#             book[count][3] = new_record
        
#         elif choice_edit_menu == 5:
#             for record in book[count]:
#                 print(f"  {record}", end = '')
#             print()

#         elif choice_edit_menu == 0:
#             search_record = False


# def remove_contact(book):
#     record_delete = input(remove_message)
#     for count in range(len(book)):
#         if record_delete == book[count][0]:
#             print(delete_message, end = '')
#             for record in book[count]:
#                 print(f"  {record}", end = '')
#             print()
#             book.pop(count)
#             return
#     print(reenter_num)

def menu_exit():
    print_message("Good bye!")