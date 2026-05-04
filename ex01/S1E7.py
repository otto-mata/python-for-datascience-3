from S1E9 import Character


class Baratheon(Character):
    """Baratheon class"""

    family_name: str
    eyes: str
    hairs: str

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(
            first_name,
            is_alive,
        )

        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        return super().die()

    def __repr__(self) -> str:
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __str__(self) -> str:
        return "coucou"


class Lannister(Character):
    """Lannister class"""

    family_name: str
    eyes: str
    hairs: str

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(
            first_name,
            is_alive,
        )

        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        return super().die()

    def __repr__(self) -> str:
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __str__(self) -> str:
        return "coucou"

    @classmethod
    def create_lannister(cls, name: str, is_alive: bool = True):
        instance = Lannister.__new__(
            cls,
        )
        instance.__init__(
            name,
            is_alive,
        )
        return instance
