
phonebook = list()

def open_file_pb(file_phonebook):
    global phonebook

    print(f"name = {file_phonebook}")    
    with open(file_phonebook, 'r', encoding='utf-8') as file:
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

    with open(file_phonebook,'w', encoding='utf-8') as file:
        file.writelines(contact)

