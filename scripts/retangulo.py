from scripts.figura_geometrica import FiguraGeometrica


class Retangulo(FiguraGeometrica):

    def __init__(self):
        self.lado_a = 0
        self.lado_b = 0

    # Retorna a area do quadrado
    def get_area(self):
        return self.lado_a * self.lado_b

    # Retorna o perimetro do quadrado
    def get_perimetro(self):
        return 2 * self.lado_a + 2 * self.lado_b