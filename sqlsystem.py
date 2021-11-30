from dbi import DatabaseInterface
from typing import Dict, Tuple
from sqldb import SqlDb
import json
from sqlalchemy.sql import text
from sqlalchemy import create_engine


class SqlDatabase(DatabaseInterface):
    """Uses sql alchemy"""

    def connect(self):
        print("-connecting to sql database")
        SqlDb()

    def disconnect(self):
        print("-Disconnecting from sql database")

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
        engine = create_engine('sqlite:///storage.db', echo=True)

        # conn = engine.connect()

        # express = text(
        #     f"SELECT data.location, data.data from data where data.location == {location}")
        # result = conn.execute(express)
        with engine.connect() as connection:
            result = connection.execute(text("select data from data"))
            for row in result:
                answer = f"location:{location} ", row['data']

        try:

            print(answer)
            reason = f"Data viewed successfully"
            print(reason)
            return True, reason, answer
        except Exception as k:
            reason = (
                f"Failed to read data in location {location}, reason: " + f"{type(k).__name__} {str(k)}")
            print(reason)
            return False, reason, ""
