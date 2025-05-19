class Editor:
    def __init__(self):
        self.texto = ""

    def escrever(self, texto):
        self.texto += texto

    def salvar(self):
        return self.texto

    def restaurar(self, estado):
        self.texto = estado


# Uso
editor = Editor()
editor.escrever("Olá ")
estado_salvo = editor.salvar()
editor.escrever("mundo!")
print(editor.texto)
editor.restaurar(estado_salvo)
print(editor.texto)
