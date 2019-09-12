"""23 - Crie uma programa que recebe uma lista qualquer e:
a. retorne o maior elemento
b. retorne a soma dos elementos
c. retorne o número de ocorrências do primeiro elemento da lista
d. retorne a média dos elementos"""

lista = []

for i in range(5):
    lista.append(int(input("Digite um número: ")))

print("O maior número é: {}".format(max(lista)))
print("Soma dos números da lista: {}".format(sum(lista)))
print("O primeiro número aparece: {} vezes".format(lista.count(lista[0])))
print("Média dos elementos: {}".format(sum(lista)/len(lista)))
