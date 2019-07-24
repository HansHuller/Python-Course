'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
testar:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
socorram me subi no onibus em marrocos
'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}

frase = str(input("Digite a frase que deseja verificar se é palíndromo: ")).strip().upper()
limpa = frase.replace(" ", "")
limpa2 = ''.join(frase.split())
inverso = ''
print("O inverso de {}{}{} é {}{}{}".format(color["cn"], limpa, color["cls"], color["ng"], limpa[::-1], color["cls"]))
if limpa == limpa[::-1]:
    print("TEMOS um palíndromo!")
else:
    print("NÃO é um palíndromo!")

for i in range(len(limpa2)-1, -1, -1):
    inverso += limpa2[i]
print("O inverso de {}{}{} é {}{}{}".format(color["cn"], limpa2, color["cls"], color["ng"], inverso, color["cls"]))
if limpa == limpa[::-1]:
    print("TEMOS um palíndromo!")
else:
    print("NÃO é um palíndromo!")
