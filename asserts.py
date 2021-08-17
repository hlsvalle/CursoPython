def smallest_item(x):
    assert x, "Lista Vazia não possui menor item"
    return min(x)

lista = [-4, 4 , 3 , -1]
lista2 = []

print(f'{"O menor valor é: "}{smallest_item(lista)}') #concatenar no python usando f-string
print("{}{} ".format("O menor valor é: ", smallest_item(lista2))) #concatenar no python usando function format
