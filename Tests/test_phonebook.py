import pytest
from phonebook import PhoneBookSystem
from filesystem import FileSystemDatabase
from unittest.mock import MagicMock
from inmemory import InmemoryDatabase


class TestPhoneBookSystem:
    database_handle = FileSystemDatabase()
    database_handle = InmemoryDatabase()
    phonebook_system = PhoneBookSystem(database_handle)

    def test_database_provider(self):
        # Prepare
        self.database_handle = FileSystemDatabase()
        self.phonebook_system = PhoneBookSystem(self.database_handle)
        self.phonebook_system.set_up_system()
        return None

    def test_create_contact(self):
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}

        output = self.phonebook_system.create_contact(data)
        expected = (True, "Contact created Succesfully ")
        assert output == expected

    @pytest.mark.skip(reason="needs a path")
    def test_fail_create_contact(self):
        name = "shone"
        phone = 1
        data = name
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.create_contact(data)
        reason = "failed to create contact"
        expected = (False, reason)
        assert output == expected

    def test_read_contact(self):
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.read_contact(data)
        excepted = (True, 'Contact read successfully', data)
        assert output == excepted

    def test_fail_read_contact(self):
        name = "Elsie"
        phone = "0788901797"
        phone2 = "0701901797"
        data = {"name": name, "phone": phone}
        data2 = {"name": name, "phone": phone2}
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.read_contact(data2)
        expected = (False, 'failed to read contact', "")
        assert output == expected

    def test_update_contact(self):
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.update_contact(data)
        expected = (True, 'Contact updated successfully')
        assert output == expected

    def test_fail_update_contact(self):
        name = "Elsie"
        name2 = "Eddie"
        phone = "0788901797"
        phone2 = "0701901797"
        data = {"name": name, "phone": phone}
        data2 = {"name": name2, "phone": phone2}
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.update_contact(data2)
        reason = 'failed to update contact'
        expected = (False, reason)
        assert output == expected

    def test_delete_contact(self):
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.delete_contact(data)
        expected = (True, 'Contact deleted successfully')
        assert output == expected

    def delete_empty_contact(self):
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        output = self.phonebook_system.delete_contact(data)
        expected = (False, 'Failed to delete contact')
        assert output == expected

    def tear_down(self) -> None:
        self.phonebook_system.tear_down_system()
        return True
