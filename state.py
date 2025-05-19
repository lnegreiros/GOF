class Estado:
    def acao(self):
        pass


class EstadoLigado(Estado):
    def acao(self):
        print("Estado: Ligado")


class EstadoDesligado(Estado):
    def acao(self):
        print("Estado: Desligado")


class Contexto:
    def __init__(self):
        self.estado = EstadoDesligado()

    def mudar_estado(self, estado):
        self.estado = estado

    def executar(self):
        self.estado.acao()


# Uso
c = Contexto()
c.executar()
c.mudar_estado(EstadoLigado())
c.executar()
