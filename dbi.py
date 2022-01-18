from abc import ABC, abstractmethod
from typing import Dict, Tuple


class DatabaseInterface(ABC):
    """Abstract class holding abstract methods"""
    @abstractmethod
    def connect(self):
        """Connects to a given storage interface"""

    @abstractmethod
    def disconnect(self):
        """Disconnects from the storage interface"""

    @abstractmethod
    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        """Create method chooses where the data will be saved and inserts the data"""

    @abstractmethod
    def read(self, location: str) -> Tuple[bool, str, Dict[str, str]]:
        """Read method chooses the location from which to read data"""

    @abstractmethod
    def update(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        """Update chooses a location and a set of data to update"""

    # @abstractmethod
    # def delete(self, location: str) -> Tuple[bool, str]:
    #     """Delete from location"""
