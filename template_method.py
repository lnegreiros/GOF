class Relatorio:
    def gerar(self):
        self.abrir()
        self.conteudo()
        self.fechar()

    def abrir(self):
        print("Abrindo relatório")

    def fechar(self):
        print("Fechando relatório")

    def conteudo(self):
        pass


class RelatorioVendas(Relatorio):
    def conteudo(self):
        print("Conteúdo: vendas do mês")


# Uso
r = RelatorioVendas()
r.gerar()
