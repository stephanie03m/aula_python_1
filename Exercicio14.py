"""13 - Escreva um algoritmo que leia as idades
de 2 homens e de 2 mulheres (considere que as
idades dos homens serão sempre diferentes entre
si, bem como as das mulheres). Calcule e escreva
a soma das idades do homem mais velho com a mulher
mais nova, e o produto das idades do homem mais
novo com a mulher mais velha."""

homem1 = int(input("Digite a idade do primeiro homem: "))

while True:
    homem2 = int(input("Digite a idade do segundo homem: "))

    if homem1 != homem2:
        break

    else:
        print("Digite uma idade diferente do primeiro homem")

mulher1 = int(input("Digite a idade da primeira mulher: "))

while True:
    mulher2 = int(input("Digite a idade da segunda mulher: "))

    if mulher1 != mulher2:
        break

    else:
        print("Digite uma idade diferente da primeira mulher")

if homem1>homem2:
    mais_velho = homem1
    mais_novo = homem2

else:
    mais_velho = homem2
    mais_novo = homem1

if mulher1>mulher2:
    mais_nova = mulher2
    mais_velha = mulher1

else:
    mais_nova = mulher1
    mais_velha = mulher2

print("Soma da idade do homem mais velho com mulher mais nova: {}".format(mais_velho+mais_nova))
print("Produto da idade do homem mais novo com mulher mais velha: {}".format(mais_novo*mais_velha))
