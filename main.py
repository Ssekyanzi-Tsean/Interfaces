from filesystem import FileSystemDatabase
from phonebook import PhoneBookSystem
from inmemory import InmemoryDatabase

#database_service = FileSystemDatabase()
database_service = InmemoryDatabase()
phonebook_system = PhoneBookSystem(database_service)
phonebook_system.set_up_system()


name = "Sean"
phone = "0772406753"
phone2 = "0774901723"
name2 = "Micheal"


phonebook_system.create_contact({"name": name, "phone": phone})
phonebook_system.read_contact({"name": name, "phone": phone})
phonebook_system.update_contact({"name": name2, "phone": phone})
phonebook_system.delete_contact({"name": name2, "phone": phone})
