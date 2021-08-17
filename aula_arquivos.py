def criar_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'a')
    texto = "Minha segunda escrita \n"
    arquivo.write(texto)
    arquivo.close()

def media_alunos(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    notas = arquivo.read()
    #print(notas)
    aluno_notas = notas.split("\n")
    #print(aluno_notas)
    for x in aluno_notas:
        lista_notas = x.split(',')
        #print(lista_notas)
        aluno = lista_notas[0] #Pegar a primeira posição da lista
        lista_notas.pop(0) #Remover a primeira posição da lista
        print('Aluno: {} '.format(aluno))
        print('Notas: {} '.format(lista_notas))
        media = lambda notas: sum([int(i) for i in notas]) / 4 #lambda para média da lista de notas convertidas em inteiro
        print('Média: {} '.format(media(lista_notas)))
        print('\n')



if __name__ == '__main__':
    #criar_arquivo('arquivo.txt')
    media_alunos('arquivo.txt')