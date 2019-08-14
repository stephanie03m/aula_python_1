"""6 - Faça um algoritmo que leia um nº inteiro e mostre uma
mensagem indicando se este número é par ou ímpar, e se é positivo
ou negativo."""

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break

    except ValueError:
        print("Digite número inteiro")

if numero>=0:
    print("{} número positivo".format(numero))

else:
    print("{} negativo".format(numero))

if numero%2==0:
    print("Par")
else:
    print("Impar")
