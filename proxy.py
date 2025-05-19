# Objeto real
class ServicoBanco:
    def operacao(self):
        return "Operação bancária realizada"

# Proxy


class ProxyBanco:
    def __init__(self, usuario):
        self.usuario = usuario
        self.banco_real = ServicoBanco()

    def operacao(self):
        if self.usuario == "admin":
            return self.banco_real.operacao()
        else:
            return "Acesso negado para usuário não autorizado"


# Uso
if __name__ == "__main__":
    cliente1 = ProxyBanco("admin")
    cliente2 = ProxyBanco("convidado")
    print(cliente1.operacao())  # Permitido
    print(cliente2.operacao())  # Negado
