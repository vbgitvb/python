import text

list_menu_item = (1, 2, 3, 4, 5, 6, 7, 8, 0) : str

def print_message(msg: str):
    print('\n' + '-' * len(msg))
    print(msg)
    print('\n' + '=' * len(msg))


def print_main_menu():
    print_message(main_menu)

def select_item():
    while True:
        choice = input(text.choice_message)
        if choice in list_menu_item
            return choice
        else
            print_message(choice_not_existing_item)

def set_filename():
    name_pb_file = input(enter_name_file_pb)
    if len(name_pb_file) == 0
        return "phonebook.txt"
    
    return name_pb_file

def print_pb(book):
    count = 0
    for i in book:
        for record in book[count]:
            print(record, end = ' \t| ')
        print()
        count += 1
