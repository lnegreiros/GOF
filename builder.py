# Produto final
class Sanduiche:
    def __init__(self):
        self.pao = None
        self.recheio = None
        self.molho = None

    def __str__(self):
        return f"Sanduíche com pão {self.pao}, recheio de {self.recheio}, e molho {self.molho}."

# Builder abstrato


class SanduicheBuilder:
    def __init__(self):
        self.sanduiche = Sanduiche()

    def preparar_pao(self): pass
    def adicionar_recheio(self): pass
    def adicionar_molho(self): pass

    def get_sanduiche(self):
        return self.sanduiche

# Builder concreto - vegetariano


class SanduicheVegetarianoBuilder(SanduicheBuilder):
    def preparar_pao(self):
        self.sanduiche.pao = "integral"

    def adicionar_recheio(self):
        self.sanduiche.recheio = "grão-de-bico e legumes"

    def adicionar_molho(self):
        self.sanduiche.molho = "azeite com ervas"

# Builder concreto - com carne


class SanduicheCarneBuilder(SanduicheBuilder):
    def preparar_pao(self):
        self.sanduiche.pao = "francês"

    def adicionar_recheio(self):
        self.sanduiche.recheio = "carne assada com queijo"

    def adicionar_molho(self):
        self.sanduiche.molho = "barbecue"

# Director


class SanduicheDirector:
    def __init__(self, builder: SanduicheBuilder):
        self.builder = builder

    def construir_sanduiche(self):
        self.builder.preparar_pao()
        self.builder.adicionar_recheio()
        self.builder.adicionar_molho()
        return self.builder.get_sanduiche()


# Uso
if __name__ == "__main__":
    escolha = input(
        "Escolha o tipo de sanduíche (vegetariano/carne): ").strip().lower()

    if escolha == "vegetariano":
        builder = SanduicheVegetarianoBuilder()
    else:
        builder = SanduicheCarneBuilder()

    diretor = SanduicheDirector(builder)
    sanduiche = diretor.construir_sanduiche()
    print(sanduiche)
