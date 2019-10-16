# -*- coding: utf-8 -*-

from unittest import TestCase
from scripts.quadrado import Quadrado


class TestQuadrado(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.fig = Quadrado()

    def test_get_area(self):
        self.fig.lado_a = 4
        self.fig.lado_b = 4
        self.assertEqual(self.fig.get_area(), 16)

    def test_get_perimetro(self):
        self.fig.lado_a = 5
        self.fig.lado_b = 5
        self.assertEqual(self.fig.get_area(), 20)
