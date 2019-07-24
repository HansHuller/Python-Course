''' Escreve um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
Ou o primeiro valor é maior
ou o segundo valor é maior
ou não existe valor maior, ambos são iguais'''

color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
n1 = int(input("{}Digite um número qualquer: ".format(color["un"])))
n2 = int(input("{}Digite outro número: {}".format(color["az"], color["cls"])))
if n1 > n2:
    print("O primeiro número ({}) é maior!!".format(n1))
elif n1 < n2:
    print("O segundo número ({}) é maior!!".format(n2))
else:
    print("Os números {} e {} são iguais!!".format(n1, n2))
