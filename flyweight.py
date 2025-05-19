class Carro:
    def __init__(self, modelo):
        self.modelo = modelo  # compartilhado (intrínseco)

    def mostrar(self, cor):
        print(f"Carro modelo {self.modelo} na cor {cor}")  # cor = extrínseco

# Flyweight Factory


class FabricaCarros:
    _carros = {}

    def get_carro(self, modelo):
        if modelo not in self._carros:
            self._carros[modelo] = Carro(modelo)
        return self._carros[modelo]


# Uso
if __name__ == "__main__":
    fabrica = FabricaCarros()
    carro1 = fabrica.get_carro("Fusca")
    carro2 = fabrica.get_carro("Fusca")
    carro1.mostrar("vermelho")
    carro2.mostrar("azul")
    print(carro1 is carro2)  # True
