from scripts.figura_geometrica import FiguraGeometrica


class Retangulo(FiguraGeometrica):
    def __init__(self):
        self.lado_a = 0
        self.lado_b = 0

    def get_area(self):
        return self.lado_a * self.lado_b

    def get_perimetro(self):
        return 2 * self.lado_a + 2 * self.lado_b


class Figura(FiguraGeometrica):
    def __init__(self):
        self.lado_a = 0
        self.lado_b = 0

    def get_area(self):
        return 2 * 3

    def get_perimetro(self):
        return None


class Example:
    def __init__(self):
        self.value = 0

    def get_area(self):
        return 2 * value


class Example2:
    pass


class Example3:
    pass


class Example4:
    pass


class Example5:
    pass


class Example6:
    pass
