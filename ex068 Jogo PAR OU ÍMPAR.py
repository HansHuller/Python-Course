'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórios consecutivas que ele conquistou no final do jogo.
'''
from random import randint
wins = 0
print("-=-="*20)
print("{:=^80}".format("JOGO DO PAR OU ÍMPAR!"))
while True:
    print("-=-=" * 20)
    computador = randint(0, 10)
    jogador = escolha = ''
    soma = 0
    while not isinstance(jogador, int):
        jogador = input("Escolha um número de 0 a 10: ")
        try:
            jogador = int(jogador)
            if not 0 <= jogador <= 10:
                jogador = ''
                print("Você digitou um número inválido, tente novamente!")
        except ValueError:
            print("Você digitou um número inválido, tente novamente!")
    while escolha != "P" and escolha != "I":
        escolha = input("Você quer PAR ou ÍMPAR [P/I]? ").upper().strip()[0]
        if escolha != "P" and escolha != "I":
            print("Você digitou um número inválido, tente novamente!")
    soma = computador + jogador
    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"
    print("~"*80)
    print(f"Você jogou {jogador} e o computador {computador}. O TOTAL é {soma} deu",
          "PAR" if resultado == "P" else "ÍMPAR")
    print("~" * 80)
    if escolha == resultado:
        wins += 1
        print("Você GANHOU! Vamos jogar novamente...")
    else:
        print("Você PERDEU! Que peninha...")
        break
if wins == 0:
    print("GAME OVER!!! Você é um fracassado! Não ganhou sequer uma vez!!! Lamentável...")
elif wins == 1:
    print(f"GAME OVER!!! Nada mal... Você ganhou {wins} vez.")
else:
    print(f"GAME OVER!!! Parabéns, saiu com saldo positivo!\nVocê ganhou {wins} vezes!")
