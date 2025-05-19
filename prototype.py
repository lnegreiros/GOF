import copy

# Classe base com método clone


class Personagem:
    def __init__(self, nome, tipo, habilidades=None):
        self.nome = nome
        self.tipo = tipo
        self.habilidades = habilidades if habilidades else []

    def adicionar_habilidade(self, habilidade):
        self.habilidades.append(habilidade)

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Personagem: {self.nome} ({self.tipo}) - Habilidades: {', '.join(self.habilidades)}"


# Uso
if __name__ == "__main__":
    # Criando um personagem base
    guerreiro = Personagem("Thor", "Guerreiro", ["Força", "Resistência"])
    print(guerreiro)

    # Clonando e personalizando
    guerreiro_clone = guerreiro.clone()
    guerreiro_clone.nome = "Hércules"
    guerreiro_clone.adicionar_habilidade("Regeneração")
    print(guerreiro_clone)

    # Original permanece inalterado
    print(guerreiro)
