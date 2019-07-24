# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
cores = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
salarioatual = float(input("Digite o salário do funcionário: R$"))
if salarioatual > 1250:
    novosalario = salarioatual*1.10
else:
    novosalario = salarioatual*1.15
print("O novo salário desse funcionário é de: {}R${:.2f}{}".format(cores["cn"], novosalario, cores["cls"]))
