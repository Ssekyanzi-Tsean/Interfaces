
from sqlalchemy.orm import session
from sqlalchemy.sql.expression import select
from dbi import DatabaseInterface
from typing import Dict, Tuple
from sqldb import SqlDb
import json
from sqlalchemy.sql import text
from sqlalchemy import create_engine, engine, update
from sqlalchemy.orm import sessionmaker


class SqlDatabase(DatabaseInterface):
    """Uses sql alchemy"""
    engine = None
    session = None

    def connect(self):
        reason = "-connecting to sql database"
        # SqlDb()
        engine = create_engine('sqlite:///storage.db', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

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
            self.session.add(handle)
            self.session.commit()
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

            result = self.session.query(SqlDb).filter(
                SqlDb.location == location).first()
            result_object = json.loads(result.data)

            reason = f"Data viewed successfully"
            print(reason)
            return True, reason, result_object
        except Exception as k:
            reason = (
                f"Failed to read data in location {location}, reason: " + f"{type(k).__name__} {str(k)}")
            print(reason)
            return False, reason, ""

    def update(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"Updating data in {location} location")
        try:

            updater = self.session.query(SqlDb).get(location)
            print("Accesing "f"{location}")
            json_loader = json.dumps(data)
            updater.data = json_loader
            self.session.commit()
            reason = f"-Data updated successful in location :{location}"
            print(reason)
            return True, reason

        except Exception as e:
            reason = (
                f"-Failed to update data in location {location}, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason)
            return False, reason

    def delete(self, location: str) -> Tuple[bool, str]:
        print(f"Deleting Contact in location {location}")
        try:
            result = self.session.query(SqlDb).filter(
                SqlDb.location == location).first()
            result_object = json.loads(result.data)

            self.session.delete(result)
            self.session.commit()
            reason = f"Data Deleted Successfully"
            print(reason)
            return True, reason
        except Exception as e:
            reason = (
                f"-Failed to Delete data in location {location}, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason)
            return False, reason
