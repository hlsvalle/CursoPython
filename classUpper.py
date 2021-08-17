class Projeto:
    def __init__(self, texto):
        self.texto = texto

    def getUpper(self):
        for i in enumerate(self.texto):
            lista = str(self.texto).upper()
        return lista

placas = ['ASB1301', 'AbS2541', 'Abs0124', 'adf7487']

projeto = Projeto(placas)

print(projeto.getUpper())

