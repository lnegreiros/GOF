from abc import ABC, abstractmethod

# Produto (Interface comum)
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Produtos concretos
class Carro(Transporte):
    def entregar(self):
        return "Entrega será feita por CARRO."

class Bicicleta(Transporte):
    def entregar(self):
        return "Entrega será feita por BICICLETA."

# Criador (Factory Method)
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self):
        transporte = self.criar_transporte()
        return transporte.entregar()

# Criadores concretos
class LogisticaRodoviaria(Logistica):
    def criar_transporte(self) -> Transporte:
        return Carro()

class LogisticaUrbana(Logistica):
    def criar_transporte(self) -> Transporte:
        return Bicicleta()

# Uso
if __name__ == "__main__":
    tipo = input("Escolha o tipo de logística (carro/bicicleta): ").strip().lower()

    if tipo == "carro":
        logistica = LogisticaRodoviaria()
    else:
        logistica = LogisticaUrbana()

    print(logistica.planejar_entrega())
