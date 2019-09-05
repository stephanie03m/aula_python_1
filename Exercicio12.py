"""12 - Ler dois valores (considere que não serão
lidos valores iguais) e escrever o maior deles. """

numero1 = int(input("Escreva um número: "))

while True:
    numero2 = int(input("Escreva outro número: "))

    if numero2 != numero1:
        break

    else:
        print("Digite um número diferente do primeiro")

if numero2 > numero1:
    print("O maior número é {}".format(numero2))

else:
    print("O maior número é {}".format(numero1))
