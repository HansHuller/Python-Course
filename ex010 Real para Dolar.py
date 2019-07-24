# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1.00 = R$3.27

wallet = float(input("Digite quanto dinheiro possue em sua carteira: R$"))
print("Com esse dinheiro você poderia comprar US${:.2f} !!!!".format(wallet/3.27))
