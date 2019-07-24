'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
n = int(input("Digite o número que deseja verificar se é primo: "))
c = 0
for i in range(1, n+1):
    if n % i == 0:
        c += 1
        print("{}{}{}".format(color["vd"], i, color["cls"]), end=" ")
    else:
        print("{}{}{}".format(color["vm"], i, color["cls"]), end=" ")
print("\nO número {} foi divisível {} vezes.".format(n, c))
if c == 2:
    print("Por isso ele é PRIMO!")
else:
    print("Por isso ele NÃO é primo!")
