
class PhoneBook:

    def __init__(self, filename: str):
        self.filename = filename if len(filename) != 0 else "phonebook.txt"
        self.content = list()

    def OpenPhoneBook(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for contact in lines:
            self.content.append(contact.strip().split(':'))
        
    def GetBook(self):
        return self.content
    
    def GetContact(self, index: int):
        return self.content[index]
    
        
    
    def GetNumbersContacts(self):
        return len(self.contetnt)

    def WriteContacts(self):
        contact = ''
        for count in range(len(self.content)):
            for record in self.content[count]:
                contact = contact + record + ':'
            contact = contact[:-1] + '\n'

        with open(self.filename,'w', encoding='utf-8') as file:
            file.writelines(contact)

    def add_contact(self, contact: list()):
        new_contact = list()
        new_contact.append(str(len(self.content)+1))
        new_contact = new_contact + contact
        self.content.append(new_contact)

    def replace(self, number: int, new_contact: list()):
        self.content[number] = new_contact

    def remove_contact(self, number: int):
        self.content.pop(number)
                
            
            

