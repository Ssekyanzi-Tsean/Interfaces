from sqlalchemy.sql.expression import select
from dbi import DatabaseInterface
from typing import Dict, Tuple
from sqldb import SqlDb
import json
from sqlalchemy.sql import text
from sqlalchemy import create_engine, engine


class SqlDatabase(DatabaseInterface):
    """Uses sql alchemy"""
    engine = create_engine('sqlite:///storage.db', echo=True)

    def connect(self):
        reason = "-connecting to sql database"
        SqlDb()
        print("Table Creation Complete")
        return True, reason

    def disconnect(self):
        reason = "-Disconnecting from sql database"
        return True, reason

    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        """creates data """
        print(f"creating data in {location} ")
        try:
            data_string = json.dumps(data)
            handle = SqlDb(location=location, data=data_string)
            SqlDb.session.add(handle)
            SqlDb.session.commit()
            reason = f"-Data created successfully in {location} location"
            print(reason)
            return (True, reason)
        except Exception as e:
            reason = (
                f"Failed to create data in location {location}, reason: " + f"{type(e).__name__} {str(e)}")
            print(reason)
            return(False, reason)

    def read(self, location: str) -> Tuple[bool, str, Dict[str, str]]:
        """Reads in data in system"""
        print(f"-Reading data in {location} location")
        row = []
        try:
            select = text(
                """SELECT location,data FROM Information WHERE location = :loc""")
            with self.engine.begin() as conn:
                for row in conn.execute(select, {"loc": location}):
                    print(row)

                reason = f"Data viewed successfully"
                print(reason)
                return True, reason, row
        except Exception as k:
            reason = (
                f"Failed to read data in location {location}, reason: " + f"{type(k).__name__} {str(k)}")
            print(reason)
            return False, reason, ""

    def update(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"Updating data in {location} location")
        try:
            with self.engine.connect() as connection:

                result = connection.execute(
                    text(f"update data SET data = :data where data.location = {location}"))
            reason = f"-Data updated successful in location :{location}"
            return True, reason
        except Exception as e:
            reason = (
                f"-Failed to update data in location {location}, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason)
            return (False, reason)
