# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sv = float(input("Digite o salário atual do funcionário: R$"))
print("O novo salário do funcionário será: R${:.2f}".format(sv*1.15))
