class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Criando nova instância...")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, valor):
        self.valor = valor

# Teste
if __name__ == "__main__":
    a = Singleton("Primeiro")
    print(f"Instância A: {a.valor}")

    b = Singleton("Segundo")
    print(f"Instância B: {b.valor}")

    print(f"Mesmo objeto? {a is b}")
