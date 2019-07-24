'''
Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinha até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''
from random import randint
from time import sleep
computador = randint(0, 10)
print("-=-"*20)
print("Vou pensar em um número entre 0 e 10.")
print("PENSANDO", end=""), sleep(0.3), print(".", end=""), sleep(0.3), print(".", end=""), sleep(0.3), print("."), sleep(0.3)
print("Pronto! Tente adivinhar...")
print("-=-"*20)
'''jogador = int(input("Em que número eu pensei?  "))
tentativas = 1
while jogador != computador:
    print("ERROOOOOUUU!!")
    if jogador < computador:
        print("Você precisa chutar um pouco mais alto para chegar lá...")
        jogador = int(input("Qual sua nova tentativa? "))
    elif jogador > computador:
        print("Tá sonhando alto? Você precisa chutar um pouco baixo para adivinhar...")
        jogador = int(input("Qual sua nova tentativa? "))
    tentativas += 1
    print("-=-"*20)
if tentativas == 1:
    print("VOCÊ ACERTOU DE PRIMEIRA!!! VOCÊ É VIDENTE???")
else:
    print("Você é fraco! Lhe falta ódio!\nVocê precisou de {} tentativas para adivinhar que eu pensei no nº {}!"
          .format(tentativas, computador))
'''
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Você precisa chutar um pouco mais alto para chegar lá...")
        elif jogador > computador:
            print("Tá sonhando alto? Você precisa chutar um pouco baixo para adivinhar...")
if tentativas == 1:
    print("VOCÊ ACERTOU DE PRIMEIRA!!! VOCÊ É VIDENTE???")
else:
    print("Você é fraco! Lhe falta ódio!\nVocê precisou de {} tentativas para adivinhar que eu pensei no nº {}!"
          .format(tentativas, computador))
