class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        sum = 0
        for x, y in zip(V1, V2):
            sum += x * y
        print("Dot product is:", sum)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Add Vector is:", [x + y for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Sous Vector is:", [x - y for x, y in zip(V1, V2)])
