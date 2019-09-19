"""Faça um programa que crie um arquivo contendo o nome
de 5 pessoas, se o nome informado for igual ao seu nome
crie outro arquivo somente com o seu nome."""

arquivo = open('C:\\Users\\ADS\\Downloads\\Stephy\\Arquivos Phyton\\CincoNomes.txt', 'w')

for i in range(5):
    nome = input("Digite um nome: ")

    if nome == "Stephy":
        arquivo_dois = open('C:\\Users\\ADS\\Downloads\\Stephy\\Arquivos Phyton\\ArquivoDois.txt', 'w')
        arquivo_dois.write(nome)
        arquivo_dois.write("\n")
        arquivo_dois.close()
    else:
        arquivo.write(nome)
        arquivo.write("\n")

arquivo.close()
