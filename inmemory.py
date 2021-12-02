from dbi import DatabaseInterface
from typing import Dict, Tuple


class InmemoryDatabase(DatabaseInterface):
    def __init__(self) -> None:
        self.data = {}

    def connect(self):
        reason = "-connecting to inmemory database"
        print(reason)
        return True, reason

    def disconnect(self):
        reason = "-Disconnecting from Inmemory Database"
        print(reason)
        return True, reason

    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"Creating data in {location} location")
        try:
            self.data[location] = data
            reason = f"Data created in {location} location"
            print(reason)
            return True, reason

        except Exception as e:
            reason = (
                f"Failed to create data in location {location}, reason: " + f"{type(e).__name__} {str(e)}")
            print(reason)
            return(False, reason)

    def read(self, location: str) -> Tuple[bool, str, Dict[str, str]]:
        print(f"Viewing data in {location} location")
        try:
            output = self.data[location]

            print(output)
            reason = f"Data viewed successfully in {location} location"
            print(reason)
            print(self.data)
            return True, reason, output
        except Exception as k:
            reason = (
                f"Failed to read data in location {location}, reason: " + f"{type(k).__name__} {str(k)}")
            print(reason)
            return False, reason, ""

    def update(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"Updating data in {location} location")
        try:
            self.data[location] = data

            reason = f"Data updated successfully in {location} location"
            print(reason)
            print(self.data)
            return True, reason
        except Exception as k:
            reason = (f"-Failed to update data in location {location}, reason: "
                      + f"{type(k).__name__} {str(k)}")
            print(reason)
            print(self.data)
            return True, reason

    def delete(self, location: str) -> Tuple[bool, str]:
        print(f"Deleting data in {location} location")
        try:
            del self.data[location]
            reason = f"Data deleted successfully in {location} location "
            return True, reason
        except Exception as k:
            reason = (f"-Failed to delete data in {location} location, reason: "
                      + f"{type(k).__name__} {str(k)}")
            print(reason)
            return False, reason
