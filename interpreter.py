class Numero:
    def __init__(self, valor):
        self.valor = valor

    def interpretar(self):
        return self.valor


class Soma:
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def interpretar(self):
        return self.esquerda.interpretar() + self.direita.interpretar()


# Uso
if __name__ == "__main__":
    expr = Soma(Numero(5), Soma(Numero(3), Numero(2)))  # 5 + (3 + 2)
    print(expr.interpretar())  # 10
