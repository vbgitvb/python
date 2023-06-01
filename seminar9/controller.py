#from text import *
import text
import model


def start():
    while runit:
        print(main_menu)
        choice_menu = int(input(text.choice_message))
        print(f"{text.choice_num_menu} {choice_menu}")

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
            print(text.good_bye)
            break
