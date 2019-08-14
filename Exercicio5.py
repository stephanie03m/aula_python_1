"""5 - Ler um valor e escrever se é positivo ou negativo
(considere o valor zero como positivo),"""

numero = float(input("Digite um número: "))

if numero>=0:
    print("{:.2f} número positivo".format(numero))

else:
    print("{:.2f} negativo".format(numero))
