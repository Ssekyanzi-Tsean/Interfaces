from filesystem import FileSystemDatabase
from phonebook import PhoneBookSystem
from inmemory import InmemoryDatabase
from sqlsystem import SqlDatabase

#database_service = FileSystemDatabase()
database_service = InmemoryDatabase()
#database_service = SqlDatabase()
phonebook_system = PhoneBookSystem(database_service)
phonebook_system.set_up_system()


name = "Sean"
phone = "0772406753"
phone2 = "0774901723"
name2 = "Micheal"
phone3 = "0741901997"


phonebook_system.create_contact({"name": name2, "phone": phone2})
phonebook_system.read_contact({"name": name2, "phone": phone2})
phonebook_system.update_contact({"name": name2, "phone": phone})
phonebook_system.delete_contact({"name": name2, "phone": phone})
