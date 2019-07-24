'''
Fala um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0
com uma pausa de 1 segundo entre eles.
'''
from time import sleep
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
for i in range(11, 0, -1):
    sleep(1)
    print(i-1)
print("É TETRAAAAAAAAAA!!!!")
