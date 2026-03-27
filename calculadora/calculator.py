

class Calculator:
    def add(self, a: float, b: float) -> float:
        
        return a + b

    def subtract(self, a: float, b: float) -> float:
        # TODO(aluno): implementar subtracao.
        
        return a - b
        

    def multiply(self, a: float, b: float) -> float:
        # TODO(aluno): implementar multiplicacao.
        
        return a * b
        

    def divide(self, a: float, b: float) -> float:
        # TODO(aluno): implementar divisao e tratar divisao por zero.
        if b == 0:
            raise ValueError("Err:. nao da pra dividir por 0")
        
        return a / b
        
        
