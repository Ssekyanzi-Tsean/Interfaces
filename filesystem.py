from dbi import DatabaseInterface
from typing import Dict, Tuple
import json
import os


class FileSystemDatabase(DatabaseInterface):
    """Uses the FileSystem as a Store"""

    def connect(self):
        print("-Connecting to file system")

    def disconnect(self):
        print("-Disconnecting from file system")

    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        """creates data"""

        print(f"Creating {location} file")
        try:
            with open(f"{location}.json", "w") as file:
                json.dump(data, file)
                reason = f"-Data created successfully in {location} location"
                print(reason)
                return (True, reason)
        except Exception as e:
            reason = (
                f"Failed to create data in location {location}, reason: " + f"{type(e).__name__} {str(e)}")
            print(reason)
            return(False, reason)

    def read(self, location: str) -> Tuple[bool, str, Dict[str, str]]:
        """reads data from sytem"""
        print(f"-Reading data in location {location}")
        results = {}
        path = f"{location}.json"

        try:
            with open(path) as file_obj:
                in_data = json.load(file_obj)
                results["output"] = file_obj
                reason = "Returned successfully"
                print(reason)
                return(True, reason, results)

        except Exception:
            reason = "No results found"
            results["output"] = ""
            print(reason)
            return(False, reason, results)

    def update(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        """update method"""
        path = f"{location}.json"
        try:
            with open(path):
                with open(path, "w") as file_object:
                    json.dump(data, file_object)
                    reason = f"-Data updated successful in location {location}"
                    print(reason)
                    return (True, reason)
        except Exception as e:
            reason = (
                f"-Failed to update data in location {location}, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason)
            return (False, reason)

    def delete(self, location: str) -> Tuple[bool, str]:
        """delete method"""
        path = f"{location}.json"
        if os.path.exists(path):
            os.remove(path)
            reason = f"-Data deleted successfully in location {location}"
            print(reason)
            return (True, reason)
        else:
            reason = "File not found"
            print(reason)
            return (False, reason)

    def tearDownSystem(self) -> None:
        print("Shutting down system")
        self.db.disconnect()
        print("System shut down complete")
