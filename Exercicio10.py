"""10 - receba três notas de um aluno e
informe se ele passou ou reprovou."""

notas = []

for i in range (3):
    notas.append(float(input("Digite a nota do aluno: ")))

if sum(notas)/3 >= 7:
    print("A média do aluno é: {:.2f}. Aprovado".format(sum(notas)/3))

else:
    print("A média do aluno é: {:.2f}. Reprovado".format(sum(notas) / 3))
