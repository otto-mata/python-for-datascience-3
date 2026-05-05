from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract character class"""

    first_name: str
    is_alive: bool

    def __init__(self, first_name: str, is_alive: bool = True):
        """Abstract class Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract die method"""
        self.is_alive = False


class Stark(Character):
    """Your docstring for Class"""

    def die(self):
        """Your docstring for Method"""
        return super().die()
