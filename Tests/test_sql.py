import pytest
from sqlsystem import SqlDatabase


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

    def test_create(self):
        location = "0701901710"
        name = "Derby"
        phone = "0701901798"
        data = {"name": name, "phone": phone}
        output = self.database.create(location, data)
        expected = True, f"-Data created successfully in {location} location"
        assert output == expected

    def test_read(self):
        pass
