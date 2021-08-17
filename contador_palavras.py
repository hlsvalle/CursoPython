def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade_letras = len(x)
        contador.append(quantidade_letras)
    return contador