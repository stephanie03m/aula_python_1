arquivo = open('C:\\Users\\ADS\\Downloads\\Stephy\\DezNomes.txt', 'w')

for i in range(10):
    arquivo.write(input("Digite um nome: "))
    arquivo.write("\n")

arquivo.close()

arquivo = open("C:\\Users\\ADS\\Downloads\\Stephy\\DezNomes.txt", "r")
for nome in arquivo:
    print(nome)
arquivo.close()
