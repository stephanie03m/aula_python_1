"""3 - Crie uma classe calculadora com as quatro operações básicas
(soma, subtração, multiplicação e divisão). O usuário deve informar
dois números e o programa deve fazer as quatro operações"""

class Calculadora():

   def soma(self,n1,n2):
       print("Resultado: {}".format(n1+n2))

   def subtracao(self,n1,n2):
       print("Resultado: {}".format(n1 - n2))

   def mutiplicacao(self,n1,n2):
       print("Resultado: {}".format(n1 * n2))

   def divisao(self,n1,n2):
       print("Resultado: {}".format(n1 / n2))

numero1 = int(input("Digite n1: "))
operacao = input("Operação +, -, *, /: ")
numero2 = int(input("Digite n2: "))

if operacao == "+":
   op = Calculadora()
   op.soma(numero1,numero2)

elif operacao == "-":
   op = Calculadora()
   op.subtracao(numero1, numero2)

elif operacao == "*":
   op = Calculadora()
   op.mutiplicacao(numero1, numero2)

elif operacao == "/":
   op = Calculadora()
   op.divisao(numero1, numero2)