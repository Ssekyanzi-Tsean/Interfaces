from dbi import DatabaseInterface
from typing import Dict, Tuple


class PhoneBookSystem:
    """PhoneBook Implemantation"""

    def __init__(self, db_service_provider: DatabaseInterface) -> None:
        """Creates a db provider instance"""
        self.db = db_service_provider

    def set_up_system(self) -> None:
        print("Starting up system")
        self.db.connect()
        print("System startup complete")

    def create_contact(self, data: dict) -> Tuple[bool, str]:
        print("Creating contact")

        phone = data["phone"]
