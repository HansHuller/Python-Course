'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
colocar timer, colocar em ordem crescente
'''
from random import randint
from time import sleep
jogos = []
teste = []
numjogos = ""
r = 0
print("="*70)
while not isinstance(numjogos, int):
    numjogos = input(f"Quantos jogos deseja fazer? ")
    try:
        numjogos = int(numjogos)
    except ValueError:
        print("Você digitou um valor inválido, digite um nº inteiro!")
print("-"*70)
print(f"{'JOGUE NA MEGA SENA - SORTEANDO JOGOS':^70}")
print("-"*70)
for i in range(0, numjogos):
    jogos.append(teste[:])
    for n in range(0, 7):
        while True:
            r = randint(1, 60)
            if r not in jogos[i]:
                break
        jogos[i].append(r)
    jogos[i].sort()
    for c in range(0,len(jogos[i])):
        if c == 0:
            print(f"Jogo Nº {i+1:<3}: [  {jogos[i][c]:>2}  ]", end="")
        else:
            print(f"[  {jogos[i][c]:>2}  ]", end="")
    print()
    sleep(0.5)
print(f"{' <Boa sorte!!!> ':=^70}")
