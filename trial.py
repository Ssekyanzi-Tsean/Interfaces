
from typing import Dict, Tuple


class InMemoryDatabase():
    def __init__(self) -> None:
        self.data = {}

    def connect(self):
        print("Connecting to In memory Database ")

    def disconnect(self):
        print("Disconnectingg from In memory Database")

    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"Creating data in Memory")

        self.data[location] = data
        reason = f"Data created Successfully in {location}"
        print(reason)
        return True, reason

    def read(self, location: str) -> Tuple[bool, Dict[str, str]]:
        print(f"-Reading data from {location}")
        location = self.data
        print(location)
        reason = f"{location} Successful"
        return True, reason

    def update(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"updating {location}")
        dicti = self.data
        dicti[location] = data
        print(dicti)
        reason = f"{location} Updated Successfully"
        return True, reason

    def delete(self, location: str) -> Tuple[bool, str]:

        results = self.data
        print(results)
        del results[location]
        print(results)
        reason = f"{location} Deleted"

        return True, reason


name = "Julius"
number = "0789034332"
location = number
data = {"name": name, "number": number}
InMemoryDatabase.create(location, data)
