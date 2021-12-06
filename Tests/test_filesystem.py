import pytest
from filesystem import FileSystemDatabase


class TestFileSystem:
    database = FileSystemDatabase()

    def test_connect(self):
        output = self.database.connect()
        expected = True, "-Connecting to file system"
        assert output == expected

    def test_disconnect(self):
        output = self.database.disconnect()
        expected = True, "-Disconnecting from file system"
        assert output == expected

    def test_create(self):
        location = "0701901797"
        name = "Malcom"
        phone = "0701901797"
        data = {"name": name, "phone": phone}
        expected = self.database.create(location, data)
        output = True, f"-Data created successfully in {location} location"
        assert expected == output

    def test_read(self):
        location = "0702456789"
        name = "Hilda"
        phone = "0702456789"
        data = {"name": name, "phone": phone}
        self.database.create(location, data)
        expected = self.database.read(location)
        output = True, "Returned successfully", data
        assert expected == output

    def test_update_contact(self):
        location = "O702456789"
        name = "Hilda"
        phone = "0702456789"
        data = {"name": name, "phone": phone}
        output = self.database.update(location, data)
        expected = True, f"-Data updated successful in location {location}"
        output == expected

    def test_delete(self):
        location = "O702456789"
        name = "Hilda"
        phone = "0702456789"
        data = {"name": name, "phone": phone}
        self.database.create(location, data)
        output = self.database.delete(location)
        expected = True, f"-Data deleted successfully in location {location}"
        assert output == expected
