from contador_palavras import contador_letras

lista_palavras = ['cachorro' , 'gato', 'elefante', 'dinossauro']

dic = {}
lista = contador_letras(lista_palavras)
i=0
for x in lista_palavras:
    dic[x] = lista[i]
    i += 1

for keys,values in dic.items():
    print('O animal ' + keys + ' tem ' + str(values) + ' letras')

