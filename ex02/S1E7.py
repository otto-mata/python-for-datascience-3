from S1E9 import Character


class Baratheon(Character):
    """Baratheon class"""

    family_name: str
    eyes: str
    hairs: str

    def __init__(self, first_name: str, is_alive: bool = True):
        """Baratheon class constructor"""
        super().__init__(
            first_name,
            is_alive,
        )

        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Baratheon class die method"""
        return super().die()

    def __repr__(self) -> str:
        """Baratheon class __repr__ method"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __str__(self) -> str:
        """Baratheon class __repr__ method"""
        return "coucou"


class Lannister(Character):
    """Lannister class"""

    family_name: str
    eyes: str
    hairs: str

    def __init__(self, first_name: str, is_alive: bool = True):
        """Lannister class constructor"""
        super().__init__(
            first_name,
            is_alive,
        )

        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Lannister class die method"""
        return super().die()

    def __repr__(self) -> str:
        """Lannister class __repr__ method"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __str__(self) -> str:
        """Lannister class __str__ method"""
        return "coucou"

    @classmethod
    def create_lannister(cls, name: str, is_alive: bool = True):
        """Create a new instance of the Lannister class"""
        instance = Lannister.__new__(
            cls,
        )
        instance.__init__(
            name,
            is_alive,
        )
        return instance
