# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

pv = float(input("Digite o valor do produto: R$"))

print("O valor do produto com desconto de 5% é de: R${:.2f}".format(pv*0.95))
