"""Escreva um algoritmo que solicita ao usuário para digitar
um número inteiro positivo, e mostre-o por extenso.
Este número deverá variar entre 1 e 5. Se o usuário introduzir
um número que não pertença a este intervalo, mostre a frase
“número inválido”."""

numero = int(input("Digite um número inteiro positivo: "))

def valor_numero(numero):

    if numero==1:
        print("1 = um")
    elif numero == 2:
        print("2 = dois")
    elif numero == 3:
        print("3 = três")
    elif numero == 4:
        print("4 = quatro")
    elif numero == 5:
        print("5 = cinco")
    else:
        print("Número inválido")

valor_numero(numero)
