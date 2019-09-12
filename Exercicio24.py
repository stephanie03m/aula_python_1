"""24 - Receba duas listas e exiba a união destas listas
e a intercalação destas listas, isto é, 1º da 1ª lista,
1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista."""

lista1 = []
lista2 = []
lista_intercalada = []

for i in range(5):
    lista1.append(input("Digite algum elemento para lista 1: "))
    lista2.append(input("Digite algum elemento para lista 2: "))

print("A união das listas: {}".format(lista1+lista2))

for i in range(5):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

print("Lista intercalada: {}".format(lista_intercalada))
