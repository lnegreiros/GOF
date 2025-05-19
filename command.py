class Luz:
    def ligar(self):
        print("Luz ligada")

    def desligar(self):
        print("Luz desligada")


class ComandoLigar:
    def __init__(self, luz):
        self.luz = luz

    def executar(self):
        self.luz.ligar()


class Controle:
    def __init__(self, comando):
        self.comando = comando

    def pressionar(self):
        self.comando.executar()


# Uso
if __name__ == "__main__":
    luz = Luz()
    comando = ComandoLigar(luz)
    controle = Controle(comando)
    controle.pressionar()
