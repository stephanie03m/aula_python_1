"""16 - Faça um algoritmo que leia os valores de COMPRIMENTO,
LARGURA e ALTURA e apresente o valor do volume de uma caixa
retangular. Utilize para o cálculo a fórmula
VOLUME = COMPRIMENTO * LARGURA * ALTURA."""

comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

print("O volume da caixa é: {}".format(comprimento*largura*altura))
