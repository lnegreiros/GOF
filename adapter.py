# Interface esperada pelo sistema
class LeitorUSB:
    def conectar_usb(self):
        pass

# Classe existente com interface diferente


class LeitorCartaoAntigo:
    def conectar_porta_serial(self):
        return "Conectado via porta SERIAL"

# Adapter que traduz de SERIAL para USB


class AdapterLeitorCartao(LeitorUSB):
    def __init__(self, leitor_antigo):
        self.leitor_antigo = leitor_antigo

    def conectar_usb(self):
        # Adapta a chamada antiga
        return self.leitor_antigo.conectar_porta_serial()

# Código cliente que espera um leitor USB


def usar_dispositivo(leitor: LeitorUSB):
    print("Sistema aguardando dispositivo USB...")
    print(leitor.conectar_usb())


# Uso
if __name__ == "__main__":
    leitor_antigo = LeitorCartaoAntigo()
    adaptado = AdapterLeitorCartao(leitor_antigo)

    usar_dispositivo(adaptado)
