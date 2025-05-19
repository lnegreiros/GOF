# Componente base
class ArquivoSistema:
    def mostrar(self):
        pass

# Folha


class Arquivo(ArquivoSistema):
    def __init__(self, nome):
        self.nome = nome

    def mostrar(self):
        print(f"Arquivo: {self.nome}")

# Composite


class Pasta(ArquivoSistema):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item: ArquivoSistema):
        self.itens.append(item)

    def mostrar(self):
        print(f"Pasta: {self.nome}")
        for item in self.itens:
            item.mostrar()


# Uso
if __name__ == "__main__":
    raiz = Pasta("raiz")
    raiz.adicionar(Arquivo("arquivo1.txt"))
    sub = Pasta("subpasta")
    sub.adicionar(Arquivo("arquivo2.txt"))
    raiz.adicionar(sub)
    raiz.mostrar()
