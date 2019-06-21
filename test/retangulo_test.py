from unittest import TestCase
from scripts.retangulo import Retangulo

class TestRetangulo(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.fig = Retangulo()

    def test_get_area(self):
        self.fig.lado_a = 5
        self.fig.lado_b = 6
        self.assertEqual(self.fig.get_area(), 30)
    def test_get_perimetro(self):
        self.fig.lado_a = 5
        self.fig.lado_b = 6
        self.assertEqual(self.fig.get_perimetro(), 22)
