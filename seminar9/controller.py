#from text import *
###import text
import view
import model

def start():
    while True:
        
        view.print_main_menu()
        choice_menu = view.select_item()

        if choice_menu == 1:
            model.open(viev.set_filename())

        elif choice_menu == 2:
            model.save(viev.set_filename())

        elif choice_menu == 3:
            view.print_pb(model.phonebook)            

        elif choice_menu == 4:
            viev.add_contact(model.phonebook)

        elif choice_menu == 5:
            if not view.print_message(" menu = 5")
                break

        elif choice_menu == 6:
            if not view.menu6()
                break

        elif choice_menu == 7:
            if not view.menu7()
                break

        elif choice_menu == 0:
            view.menu_exit()
            break
