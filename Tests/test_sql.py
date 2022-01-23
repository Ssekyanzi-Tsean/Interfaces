from venv import create
import pytest
from app.sqlsystem import SqlDatabase


class TestSqlDatabase:
    database = SqlDatabase()

    def test_connect(self):
        output = self.database.connect()
        expected = True, "-connecting to sql database"
        assert output == expected

    def test_disconnect(self):
        output = self.database.disconnect()
        expected = True, "-Disconnecting from sql database"
        assert output == expected

    # @pytest.mark.skip(reason="")
    def test_create(self):
        location = "0772129076"
        name = "Andrew"
        phone = "0772129076"
        data = {"name": name, "phone": phone}
        output = self.database.create(location, data)
        expected = True, f"-Data created successfully in {location} location"
        assert output == expected
        cleanup = self.database.delete(location)

    def test_read(self):
        location = "0773405662"
        name = "Sharon"
        phone = "0773405612"
        data = {"name": name, "phone": phone}
        creater = self.database.create(location, data)
        output = self.database.read(location)
        expected = True, f"Data viewed successfully", data
        assert output == expected
        cleanup = self.database.delete(location)

    # @pytest.mark.skip(reason="")
    def test_update(self):
        location = "0772404987"
        phone = "0772404987"
        name = "Sharon"
        name2 = "Alex"
        phone2 = "0702404987"
        data = {"name": name, "phone": phone}
        data2 = {"name": name2, "phone": phone}
        creater = self.database.create(location, data)
        output = self.database.update(location, data2)
        expected = True, f"-Data updated successful in location :{location}"
        cleanup = self.database.delete(location)

    def test_delete(self):
        location = "0760198762"
        phone = "0760198762"
        name = "Godwin"
        data = {"name": name, "phone": phone}
        creater = self.database.create(location, data)
        output = self.database.delete(location)
        expected = True, f"Data Deleted Successfully"
