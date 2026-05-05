from typing import Any


class calculator:
    """Calculator class"""

    def __init__(self, v: list[float]) -> None:
        """Class construtor"""
        self.v = v

    def __add__(self, object: Any) -> None:
        """Add a scalar value to self and print the result"""
        assert isinstance(
            object,
            (
                float,
                int,
            ),
        ), "Wrong type"
        self.v = [x + object for x in self.v]
        print(self.v)
        return None

    def __mul__(self, object: Any) -> None:
        """Multiply a scalar value to self and print the result"""
        assert isinstance(
            object,
            (
                float,
                int,
            ),
        ), "Wrong type"
        self.v = [x * object for x in self.v]
        print(self.v)
        return None

    def __sub__(self, object: Any) -> None:
        """Substract a scalar value from self and print the result"""
        assert isinstance(
            object,
            (
                float,
                int,
            ),
        ), "Wrong type"
        self.v = [x - object for x in self.v]
        print(self.v)
        return None

    def __truediv__(self, object: Any) -> None:
        """Divide self by a scalar value and print the result"""
        assert isinstance(
            object,
            (
                float,
                int,
            ),
        ), "Wrong type"
        assert object != 0, "Zero division error"
        self.v = [x / object for x in self.v]
        print(self.v)
        return None
