# Componente base
class Cafe:
    def custo(self):
        return 5

# Decorator base


class Decorador(Cafe):
    def __init__(self, cafe):
        self.cafe = cafe

# Decoradores concretos


class ComLeite(Decorador):
    def custo(self):
        return self.cafe.custo() + 2


class ComChocolate(Decorador):
    def custo(self):
        return self.cafe.custo() + 3


# Uso
if __name__ == "__main__":
    pedido = Cafe()
    pedido = ComLeite(pedido)
    pedido = ComChocolate(pedido)
    print(f"Total: R${pedido.custo()}")  # Total: R$10
