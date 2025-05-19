class Manipulador:
    def __init__(self, sucessor=None):
        self.sucessor = sucessor

    def tratar(self, nivel):
        if self.sucessor:
            return self.sucessor.tratar(nivel)
        return "Sem manipulador disponível"


class NivelAlerta(Manipulador):
    def tratar(self, nivel):
        if nivel == "alerta":
            return "Tratado por Alerta"
        return super().tratar(nivel)


class NivelCritico(Manipulador):
    def tratar(self, nivel):
        if nivel == "crítico":
            return "Tratado por Crítico"
        return super().tratar(nivel)


# Uso
if __name__ == "__main__":
    cadeia = NivelAlerta(NivelCritico())
    print(cadeia.tratar("crítico"))  # Tratado por Crítico
