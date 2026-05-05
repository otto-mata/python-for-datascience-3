class calculator:
    """Calculator utils class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors represented by lists
        and print the resulting value."""
        sum = 0
        for x, y in zip(V1, V2):
            sum += x * y
        print("Dot product is:", sum)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors represented by lists and print the resulting
        vector."""
        print("Add Vector is:", [x + y for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substract V2 from V1, two vectors represented by lists and print
        the resulting vector."""
        print("Sous Vector is:", [x - y for x, y in zip(V1, V2)])
