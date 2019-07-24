''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 = binário ;   2 = octal ; 3 = hexadecimal'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
num = int(input("Digite o número que deseja converter: "))
print("Em qual formato você deseja transformar o número {}?\n"
      "Digite 1 para binário\n"
      "Digite 2 para octal\n"
      "Digite 3 para hexadecimal\n".format(num))
escolha = int(input("Qual a sua escolha?"))
if escolha == 1:
    print("O número {} em binário é: {}".format(num, bin(num)[:2]))
elif escolha == 2:
    print("O número {} em octal é: {}".format(num, oct(num)[:2]))
elif escolha == 3:
    print("O número {} em hexadecimal é: {}".format(num, hex(num)[:2]))
else:
    print("Você não selecionou uma opção válida. Tente novamente!")
