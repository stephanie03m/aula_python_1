"""7 - Escreva um algoritmo que leia 10 números informados
pelo usuário e, depois, informe o menor, número, o maior
número, a soma dos números informados e a média aritmética
dos números informados."""

numero = []

while len(numero) < 10:
    try:
        numero.append(int(input("Digite um número: ")))

    except ValueError:
        print("Não é um valor válido")

print("O maior número é: {}".format(max(numero)))
print("O menor número é: {}".format(min(numero)))
print("Soma dos números: {}".format(sum(numero)))
print("Média aritmética: {}".format((sum(numero)/len(numero))))