from filesystem import FileSystemDatabase
from phonebook import PhoneBookSystem


database_service = FileSystemDatabase()
phonebook_system = PhoneBookSystem(database_service)
phonebook_system.set_up_system()


name = "Sean"
phone = "0772406753"

phonebook_system.create_contact({"name": name, "phone": phone})
