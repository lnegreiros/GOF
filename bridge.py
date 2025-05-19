# Implementação
class Cor:
    def aplicar_cor(self):
        pass


class Vermelho(Cor):
    def aplicar_cor(self):
        return "vermelho"


class Azul(Cor):
    def aplicar_cor(self):
        return "azul"

# Abstração


class Forma:
    def __init__(self, cor: Cor):
        self.cor = cor

    def desenhar(self):
        pass


class Circulo(Forma):
    def desenhar(self):
        return f"Desenhando círculo na cor {self.cor.aplicar_cor()}"


# Uso
if __name__ == "__main__":
    forma = Circulo(Vermelho())
    print(forma.desenhar())  # "Desenhando círculo na cor vermelho"
