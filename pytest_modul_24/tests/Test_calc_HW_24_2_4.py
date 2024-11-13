import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 2) == 10

    def test_division(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(self, 5, 3) == 2