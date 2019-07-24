''' Crie um programa que faça o computador jogar Jokenpô com você'''
'''color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
from time import sleep
from random import shuffle
print("{:=^40}".format("JOGO DE JOKENPÔ"))
cpu = ["PEDRA", "PAPEL", "TESOURA"]
jog = str(input("\nSuas opções: "
                "\nPEDRA"
                "\nPAPEL"
                "\nTESOURA"
                "\nQual a sua escolha? ")).upper()
shuffle(cpu)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")

if cpu[0] == jog:
    res = 2
elif cpu[0] == "PEDRA" and jog == "TESOURA":
    res = 0
elif cpu[0] == "PEDRA" and jog == "PAPEL":
    res = 1
elif cpu[0] == "PAPEL" and jog == "PEDRA":
    res = 0
elif cpu[0] == "PAPEL" and jog == "TESOURA":
    res = 1
elif cpu[0] == "TESOURA" and jog == "PAPEL":
    res = 0
elif cpu[0] == "TESOURA" and jog == "PEDRA":
    res = 1
print("-="*20, "\nO computador jogou {}!\nO jogador jogou {}".format(cpu[0], jog))
print("-="*20)
if res == 2:
    print("Isso resulta em um EMPATE!")
elif res == 1:
    print("O JOGADOR VENCEU!!")
else:
    print("O JOGADOR PERDEU!!")
'''
from random import randint
from time import sleep
jogada = ("PEDRA", "PAPEL", "TESOURA")
cpu = randint(0,2)
jog = int(input("\nSuas opções: "
                "\n[ 0 ] PEDRA"
                "\n[ 1 ] PAPEL"
                "\n[ 2 ] TESOURA"
                "\nQual a sua escolha? "))
if jog > 2:
    print("Você selecionou uma opção inválida, tente novamente!")
    quit()
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")
print("-="*20, "\nO computador jogou {}!\nO jogador jogou {}".format(jogada[cpu], jogada[jog]))
print("-="*20)

if jogada[cpu] == jogada[jog]:
    print("Isso resulta em um EMPATE!")
elif cpu == 0:
    if jog == 1:
        print("O JOGADOR VENCEU!!")
    if jog == 2:
        print("O JOGADOR PERDEU!!")
elif cpu == 1:
    if jog == 0:
        print("O JOGADOR PERDEU!!")
    if jog == 2:
        print("O JOGADOR VENCEU!!")
elif cpu == 2:
    if jog == 0:
        print("O JOGADOR VENCEU!!")
    if jog == 1:
        print("O JOGADOR PERDEU!!")
else:
    print("Você digitou uma opção inválida!")
