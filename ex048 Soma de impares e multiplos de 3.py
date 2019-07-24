'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
s = 0
for i in range(1, 501):
    if (i % 2) == 1 and (i % 3) == 0:
        s += i
print("A soma é igual à: {}".format(s))

s = 0
for i in range(0, 501, 3):
    if (i % 2) == 1:
        s += i
print("A soma é igual à: {}".format(s))
