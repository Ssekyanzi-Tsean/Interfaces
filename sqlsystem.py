from dbi import DatabaseInterface
from typing import Dict, Tuple
from sqldb import SqlDb
import json


class SqlDatabase(DatabaseInterface):
    """Uses sql alchemy"""

    def connect(self):
        print("-connecting to sql database")
        SqlDb

    def disconnect(self):
        print("-Disconnecting from sql database")

    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        """creates data """
        print(f"creating data in {location} ")
        try:
            data_string = json.dump(data)
            handle = SqlDb(location=location, data=data_string)
            reason = f"-Data created successfully in {location} location"
            print(reason)
            return (True, reason)
        except Exception as e:
            reason = (
                f"Failed to create data in location {location}, reason: " + f"{type(e).__name__} {str(e)}")
            print(reason)
            return(False, reason)
