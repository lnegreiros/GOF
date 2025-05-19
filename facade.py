class CPU:
    def ligar(self):
        print("CPU ligada")


class Memoria:
    def carregar(self):
        print("Memória carregada")


class Disco:
    def ler(self):
        print("Disco lido")

# Fachada


class Computador:
    def iniciar(self):
        print("Iniciando computador...")
        CPU().ligar()
        Memoria().carregar()
        Disco().ler()


# Uso
if __name__ == "__main__":
    computador = Computador()
    computador.iniciar()
