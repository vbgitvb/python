

#file_phonebook = "phonebook.txt"

phonebook = list()


# def init_pb(name_of_pb: str):
#     if len(name_of_pb) == 0
#         file_phonebook = "phonebook.txt"
#     else
#         file_phonebook = name_of_pb


def open(file_phonebook :str):
    global phonebook
    
    with open(file_phonebook,'r', encoding='utf-8') as file:
        lines = file.readlines()

    for contact in lines:
        phonebook.append(contact.strip().split(':'))


def save(file_phonebook :str):
    global phonebook
    contact = ""

    for count in range(len(phonebook)):
        for record in phonebook[count]:
            contact = contact + record + ':'
        contact = contact[:-1] + '\n'

    with open(filename,'w', encoding='utf-8') as file:
        file.writelines(contact)

