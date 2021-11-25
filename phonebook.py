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

        created, reason = self.db.create(phone, data)
        if not created:
            print(reason)
            return False, reason

        reason = "Contact created Succesfully "
        print(reason)
        return True, reason

    def update_contact(self, data: Dict[str, str]) -> Tuple[bool, str]:
        """Update method """
        print("Updating contact")
        phone = data["phone"]
        print(phone)
        updated, reason = self.db.update(phone, data)
        print(reason)
        if not updated:
            print(reason)
            reason = "failed to update contact"
            return False, reason

        reason = "Contact updated successfully"
        print(reason)
        return True, reason
