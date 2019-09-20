"""Faça a tabuada de 1 até 10 e salve cada uma
em um arquivo, depois leia e mostre na tela"""

for i in range(1, 11, 1):
    arquivo = open('C:\\Users\\ADS\\Downloads\\Stephy\\Arquivos Phyton\\' + str(i) + '.txt', 'w')

    for x in range(1, 11, 1):
        resultado = i * x
        arquivo.write(str(i) + " X " + str(x) + " = " + str(resultado)+ "\n")

    arquivo.write("------------")
    arquivo.close()

for i in range(1, 11, 1):
    arquivo = open('C:\\Users\\ADS\\Downloads\\Stephy\\Arquivos Phyton\\' + str(i) + '.txt', 'r')

    for linha in arquivo:
        print(linha)

    arquivo.close()
    
