class EstrategiaSoma:
    def executar(self, a, b):
        return a + b


class EstrategiaMultiplica:
    def executar(self, a, b):
        return a * b


class Calculadora:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, a, b):
        return self.estrategia.executar(a, b)


# Uso
c = Calculadora(EstrategiaSoma())
print(c.calcular(2, 3))  # 5
c = Calculadora(EstrategiaMultiplica())
print(c.calcular(2, 3))  # 6
