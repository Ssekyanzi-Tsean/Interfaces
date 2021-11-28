from dbi import DatabaseInterface
from typing import Dict, Tuple


class InmemoryDatabase():
    def __init__(self) -> None:
        super(). __init__()
        self.data = {}
        __instance = None

    @staticmethod
    def check_instance():
        if InmemoryDatabase.__instance is None:
            return InmemoryDatabase()
        return InmemoryDatabase.__instance

    def connect(self):
        print("-connecting to inmemory database")
        return True

    def disconnect(self):
        print("-Disconnecting from Inmemory Database")
        return True

    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"Creating data in {location} location")
        try:
            print(self.data[location])
            reason = "failed to create data in location"
            print(reason)
            return False, reason
        except Exception:
            self.data[location] = data
            print(self.data)
            reason = f"Data created successfully in {location} location"
            print(reason)
            return True, reason

    def read(self, location: str) -> Tuple[bool, str, Dict[str, str]]:
        print(f"Viewing data in {location} location")
        print(self.data)
        try:
            print(self.data[location]["phone"])
            reason = f"Data viewed successfully in {location} location"
            print(reason)
            print(self.data)
            return True, reason, self.data
        except Exception as k:
            reason = (
                f"Failed to read data in location {location}, reason: " + f"{type(k).__name__} {str(k)}")
            print(reason)
            return (False, reason, "")

    def update(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"Updating data in {location} location")
        print(self.data)

        try:
            print(self.data[location]["phone"])
            self.data[location] = data
            print(self.data)
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
