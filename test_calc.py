import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiplay_success(self):
        assert self.calc.multiply(self, 8, 7) == 56

    def test_division_success(self):
        with pytest.raises(ZeroDivisionError): # 'raises' обрабатывает ошибки
            self.calc.division(self, 1, 0)

    def test_sutraction_success(self):
        assert self.calc.sutraction(self, 56, 16) == 40

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def teardown(self):
        print('Выполнение метода Teardown')