# -*- coding: utf-8 -*-
import math
from scripts.figura_geometrica import FiguraGeometrica


class Circulo(FiguraGeometrica):
    def __init__(self):
        self.raio = 0

    def get_area(self):
        return math.pi * self.raio ** 2

    def get_perimetro(self):
        return 2 * math.pi * self.raio
