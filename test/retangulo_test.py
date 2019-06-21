from unittest import TestCase
from scripts.retangulo import Retangulo

class TestRetangulo(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.fig = Retangulo()
