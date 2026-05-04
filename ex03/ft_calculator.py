from typing import Any


class calculator:
    """Calculator class"""

    def __init__(self, v: list[float]) -> None:
        self.v = v

    def __add__(self, object: Any) -> None:
        """__add__ method"""
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
        """__mul__ method"""
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
        """__sub__ method"""
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
        """__truediv__ method"""
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


v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
