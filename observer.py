class Sujeito:
    def __init__(self):
        self.observadores = []
        self.estado = ""

    def anexar(self, obs):
        self.observadores.append(obs)

    def notificar(self):
        for o in self.observadores:
            o.atualizar(self.estado)

    def mudar_estado(self, valor):
        self.estado = valor
        self.notificar()


class Observador:
    def atualizar(self, valor):
        print(f"Recebido: {valor}")


# Uso
s = Sujeito()
s.anexar(Observador())
s.mudar_estado("Novo estado!")
