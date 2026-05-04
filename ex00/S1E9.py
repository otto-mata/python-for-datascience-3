from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    first_name: str
    is_alive: bool

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        self.is_alive = False


class Stark(Character):
    """Your docstring for Class"""

    def die(self):
        """Your docstring for Method"""
        return super().die()
