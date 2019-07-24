# Escreva um programa que faça o computador "pensar" erm um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

num = randint(0, 5)
print("-=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
adv = int(input("Em que número eu pensei?  "))
print("PROCESSANDO", end=""),sleep(1),print(".", end=""),sleep(1),print(".", end=""),sleep(1),print("."),sleep(1)
print("-=-"*20)
if adv == num:
    print("VOCÊ ACERTOU!!! VOCÊ É VIDENTE???")
else:
    print("Você é fraco! Lhe falta ódio!\nEu pensei em {} não em {}".format(num, adv))
