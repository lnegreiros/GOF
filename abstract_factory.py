from abc import ABC, abstractmethod

# Interfaces dos produtos


class Botao(ABC):
    @abstractmethod
    def renderizar(self):
        pass


class CaixaTexto(ABC):
    @abstractmethod
    def renderizar(self):
        pass

# Produtos concretos para Windows


class BotaoWindows(Botao):
    def renderizar(self):
        return "Renderizando botão no estilo Windows"


class CaixaTextoWindows(CaixaTexto):
    def renderizar(self):
        return "Renderizando caixa de texto no estilo Windows"

# Produtos concretos para Mac


class BotaoMac(Botao):
    def renderizar(self):
        return "Renderizando botão no estilo MacOS"


class CaixaTextoMac(CaixaTexto):
    def renderizar(self):
        return "Renderizando caixa de texto no estilo MacOS"

# Fábrica abstrata


class GUIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_caixa_texto(self) -> CaixaTexto:
        pass

# Fábricas concretas


class WindowsFactory(GUIFactory):
    def criar_botao(self) -> Botao:
        return BotaoWindows()

    def criar_caixa_texto(self) -> CaixaTexto:
        return CaixaTextoWindows()


class MacFactory(GUIFactory):
    def criar_botao(self) -> Botao:
        return BotaoMac()

    def criar_caixa_texto(self) -> CaixaTexto:
        return CaixaTextoMac()

# Aplicação


def renderizar_interface(factory: GUIFactory):
    botao = factory.criar_botao()
    caixa_texto = factory.criar_caixa_texto()
    print(botao.renderizar())
    print(caixa_texto.renderizar())


# Simulação de escolha do sistema operacional
if __name__ == "__main__":
    sistema = input("Escolha o sistema (windows/mac): ").strip().lower()

    if sistema == "windows":
        factory = WindowsFactory()
    else:
        factory = MacFactory()

    renderizar_interface(factory)
