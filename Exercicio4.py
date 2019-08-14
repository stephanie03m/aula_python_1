"""4 - Faça um programa que receba um valor que é o valor pago,
um segundo valor que é o preço do produto e retorne o troco
a ser dado."""

while True:
    try:
        preco_produto = float(input("Digite o preço do produto: "))
        break

    except ValueError:
        print("Digite valores")

while True:
    try:
        valor_pago = float(input("Digite o valor pago: "))
        if valor_pago>=preco_produto:
            break
        else:
            print("Valor insuficiente")

    except ValueError:
        print("Digite valores")

print("Preço do produto: R$ {:.2f} ".format(preco_produto))
print("Valor pago: {:.2f}".format(valor_pago))
print("Valor do troco: {:.2f}".format(valor_pago - preco_produto))
