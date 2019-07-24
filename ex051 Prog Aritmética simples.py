'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PROGRESSÃO ARITMÉTICA.
No final mostre os 10 primeiros termos dessa progressão.
'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
t = int(input("Digite o primeiro termo da Progressão aritmética: "))
r = int(input("Digite a razão: "))
n = int(input("Digite até qual termo? "))
enezimo = t + (n-1) * r
pa = t
'''for i in range(1, 11):
    print("{}".format(pa), end=" → ")
    pa += r
print("ACABOU!!")'''

for i in range(t, enezimo+1, r):
    print("{}".format(i), end=" → ")
print("ACABOU!!")
