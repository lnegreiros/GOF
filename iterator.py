class ColecaoNomes:
    def __init__(self):
        self.nomes = ["Ana", "Bruno", "Carlos"]

    def __iter__(self):
        return iter(self.nomes)


# Uso
for nome in ColecaoNomes():
    print(nome)
