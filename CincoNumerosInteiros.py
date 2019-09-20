""Escreva um programa que receba do usuário 5 números inteiros
e o nome do arquivo no qual eles devem ser armazenados.
Em seguida, ler do arquivo estes valores armazenados copiando-os
para um vetor de inteiros e imprimindo na tela."""

nome_arquivo = input("Digite o nome do arquivo: ")

arquivo = open('C:\\Users\\ADS\\Downloads\\Stephy\\Arquivos Phyton\\' + nome_arquivo + '.txt', 'w')

for i in range(5):
    arquivo.write(input("Digite um numero: "))
    arquivo.write("\n")

arquivo.close()

arquivo = open('C:\\Users\\ADS\\Downloads\\Stephy\\Arquivos Phyton\\' + nome_arquivo + '.txt', 'r')

lista = []

for nome in arquivo:
    lista.append(nome)

arquivo.close()

print("\n")
print("Os números são: ")

for linhas in lista:
    print(linhas)
    
