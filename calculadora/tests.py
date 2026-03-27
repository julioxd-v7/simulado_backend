from django.test import TestCase

from .calculator import Calculator



a = 4
b = 2

class CalculatorTests(TestCase):
    def add(self, a: float, b: float) -> float:
        
        return a + b

    def subtract(self, a: float, b: float) -> float:
        
        return a - b
        

    def multiply(self, a: float, b: float) -> float:
        
        return a * b
        

    def divide(self, a: float, b: float) -> float:
        
        if b == 0:
            raise ValueError("Err:. nao da pra dividir por 0")
        
        return a / b
        
        
