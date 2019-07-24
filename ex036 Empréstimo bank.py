''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa
vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
'''
from math import ceil

vcasa = float(input("Por favor digite o valor da casa que deseja adiquirir: \033[0;33mR$\033[m"))
salario = float(input("Me informe o seu salário: R$"))
anos = int(input("Digite em quantos anos deseja pagar: "))
mensalidade = vcasa / (anos*12)
sal30 = salario*0.3

print(("-=-"*20),"\nPara pagar uma casa de R${:.2f} em {} anos a mensalidade seria de R${:.2f}".format(vcasa, anos, mensalidade))
if sal30 >= mensalidade:
    print("Parabéns seu empréstimo foi aprovado!")
else:
    print(("-=-"*20),"\nDesculpe mas seu empréstimo foi negado!\nPara conseguir o empréstimo você teria"
                     " que pagar em {} meses\n"
          "Aproximadamente {} anos"
          .format(ceil(vcasa/sal30), ceil(vcasa/sal30/12)))
