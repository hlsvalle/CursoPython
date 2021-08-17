class CountingClicker: #Criando a classe
    def __init__(self, count = 0): #construtor da classe
        self.count = count

    # definir metodos publicos
    def click(self, num_times=1):
        """Incrementando o numero de cliques"""
        self.count += num_times

    # Ler o valor de count
    def read(self):
        return self.count

    # Resetar  o numero de cliques
    def reset(self):
        self.count = 0



clicker = CountingClicker() #inicializando a classe com o valor 0
print(clicker.read())
assert clicker.read() == 0, "clicker devera iniciar com zero"
clicker.click() # Primeiro clique, valor devera estar em 1
print(clicker.read())
assert clicker.read() == 1, "clicker devera estar em 1"
clicker.reset()
print(clicker.read())
assert clicker.read() == 0, "otimo foi resetado e valor esta em 0"

