import text
import view
import model

def start():
    while True:
        
        view.print_main_menu()
        choice_menu = view.select_item()

        if choice_menu == 1:
            model.open_file_pb(view.set_filename())
            view.print_message(text.open_without_error)

        elif choice_menu == 2:
            model.save(view.set_filename())

        elif choice_menu == 3:
            view.print_pb(model.phonebook)            

        elif choice_menu == 4:
            view.add_contact(model.phonebook)

        elif choice_menu == 5:
            pass

        elif choice_menu == 6:
            view.edit_contact(model.phonebook)

        elif choice_menu == 7:
            view.remove_contact(model.phonebook)

        elif choice_menu == 0:
            view.menu_exit()
            break
