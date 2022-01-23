import pytest
from app.inmemory import InmemoryDatabase


class TestInmemoryDatabase:
    database = InmemoryDatabase()

    def test_connect(self):
        output = self.database.connect()
        excepted = (True, "-connecting to inmemory database")
        assert output == excepted

    def test_disconnect(self):
        output = self.database.disconnect()
        expected = (True, "-Disconnecting from Inmemory Database")
        assert output == expected

    def test_create(self):
        location = "0701901797"
        phone = "0701901797"
        name = "Tchami"
        data = {"name": name, "phone": phone}
        output = self.database.create(location, data)
        expected = (True, f"Data created in {location} location")
        assert output == expected

    def test_read(self):
        location = "0772404987"
        name = "Morrison"
        phone = "0772404987"
        data = {"name": name, "phone": phone}
        self.database.create(location, data)
        output = self.database.read(location)
        expected = True, f"Data viewed successfully in {location} location", data
        assert output == expected

    def test_update(self):
        location = "0772404987"
        name = "Morrison"
        name2 = "Arrdee"
        phone = "0702404987"
        phone2 = "074123456"
        data = {"name": name, "phone": phone}
        data2 = {"name": name, "phone": phone2}
        self.database.create(location, data)
        self.database.read(location)
        output = self.database.update(location, data2)
        expected = True, f"Data updated successfully in {location} location"
        assert output == expected

    def test_delete(self):
        location = "0772404987"
        name = "Arrdee"
        phone = "0772404987"
        data = {"name": name, "phone": phone}
        self.database.create(location, data)
        output = self.database.delete(location)
        expected = True, f"Data deleted successfully in {location} location "
        assert output == expected
