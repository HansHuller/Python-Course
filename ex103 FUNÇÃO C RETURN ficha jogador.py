'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

'''

def ficha(jogador = "<desconhecido>", gols = 0):
    if jogador.strip() == "":
        jogador = "<desconhecido>"
    if not gols.isnumeric():
        gols = 0
    return f"O jogador {jogador} marcou {gols} gol(s) no campeonato."


# Programa Principal


print(ficha(str(input("Nome do jogador: ")), input("Número de gols: ")))
