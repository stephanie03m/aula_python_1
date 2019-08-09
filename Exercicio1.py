"""Escreva uma classe que contém um método que calcule se a pessoa
é maior de 18 anos ou não. Receba os dados pela console e chame
este método. """


idade = int(input("Digite sua idade: "))

def valor_idade(idade):

   if idade>18:
       print("Maior que 18 anos")
   else:
       print("Menor que 18 anos")

valor_idade(idade)



