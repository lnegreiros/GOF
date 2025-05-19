class ChatMediator:
    def enviar(self, msg, usuario):
        for u in self.usuarios:
            if u != usuario:
                u.receber(msg)

    def __init__(self):
        self.usuarios = []

    def adicionar(self, usuario):
        self.usuarios.append(usuario)


class Usuario:
    def __init__(self, nome, chat):
        self.nome = nome
        self.chat = chat
        self.chat.adicionar(self)

    def enviar(self, msg):
        print(f"{self.nome} envia: {msg}")
        self.chat.enviar(msg, self)

    def receber(self, msg):
        print(f"{self.nome} recebe: {msg}")


# Uso
if __name__ == "__main__":
    chat = ChatMediator()
    u1 = Usuario("João", chat)
    u2 = Usuario("Maria", chat)
    u1.enviar("Oi!")
