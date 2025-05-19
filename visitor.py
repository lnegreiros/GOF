class Forma:
    def aceitar(self, visitante):
        pass


class Circulo(Forma):
    def aceitar(self, visitante):
        visitante.visitar_circulo(self)


class Retangulo(Forma):
    def aceitar(self, visitante):
        visitante.visitar_retangulo(self)


class Desenhador:
    def visitar_circulo(self, c):
        print("Desenhando círculo")

    def visitar_retangulo(self, r):
        print("Desenhando retângulo")


# Uso
formas = [Circulo(), Retangulo()]
visitante = Desenhador()
for f in formas:
    f.aceitar(visitante)
