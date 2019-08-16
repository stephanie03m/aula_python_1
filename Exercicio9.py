"""9 - Faça um método que receba um número X
e uma palavra no console e repita x vezes
essa frase."""


def varios_nomes():

    numero = int(input("Digite um número : "))
    palavra = input("Digite uma palavra: ")

    for i in range(numero):
        print(palavra)

if __name__ == "__main__":
    varios_nomes()