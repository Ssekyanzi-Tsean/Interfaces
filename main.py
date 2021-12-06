from filesystem import FileSystemDatabase
from phonebook import PhoneBookSystem
from inmemory import InmemoryDatabase
from sqlsystem import SqlDatabase

#database_service = FileSystemDatabase()
#database_service = InmemoryDatabase()
database_service = SqlDatabase()
phonebook_system = PhoneBookSystem(database_service)
phonebook_system.set_up_system()


name = "Tchami"
phone = "0778901797"
name2 = "Bernado"
phone2 = "0701901797"
name3 = "Kingsley"
phone3 = "0788357684"


#phonebook_system.create_contact({"name": name3, "phone": phone3})
phonebook_system.read_contact({"name": name3, "phone": phone3})
#phonebook_system.update_contact({"name": name3, "phone": phone4})
#phonebook_system.delete_contact({"name": name2, "phone": phone})
