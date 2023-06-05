import text
import view
import model


MyPhBook = model.PhoneBook("phonebook.txt")

def start():
    while True:
        
        view.print_main_menu()
        choice_menu = view.select_item()

        if choice_menu == 1:
            MyPhBook.OpenPhoneBook()
            view.print_message(text.open_without_error)

        elif choice_menu == 2:
            MyPhBook.WriteContacts()

        elif choice_menu == 3:
            view.print_pb(MyPhBook.GetBook())            

        elif choice_menu == 4:
            MyPhBook.add_contact(view.enter_new_contact())

        elif choice_menu == 5:
            pass

        elif choice_menu == 6:
            num_edit_contact = view.get_num_contact(text.edit_message)
            edit_contact = MyPhBook.GetContact(num_edit_contact)
            MyPhBook.replace(num_edit_contact, view.choice_item_edit(edit_contact))

        elif choice_menu == 7:
            num_remove_contact = view.get_num_contact(text.remove_message)
            MyPhBook.remove_contact(num_remove_contact)

        elif choice_menu == 0:
            view.menu_exit()
            break
