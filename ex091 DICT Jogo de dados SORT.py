'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
Programa não faz leitura, simula os jogadores jogando os dados e exibe o ranking deles.
'''
from time import sleep
from random import randint
from operator import itemgetter
jogadores = {"Jogador 1": randint(1, 6),
             "Jogador 2": randint(1, 6),
             "Jogador 3": randint(1, 6),
             "Jogador 4": randint(1, 6)}
print("Valores tirados: ")
sleep(0.5)
for k, v in jogadores.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(0.5)
print("=-=-="*14)
print(f"{'RANKING DOS JOGADORES':=^70}")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
rankingv2 = sorted(jogadores.items(), key=lambda i: i[1], reverse=True)
for k, v in enumerate(ranking):
    print(f"{k+1}º Lugar para o {v[0]} com o valor {v[1]}")
print("="*70)
for k, v in enumerate(rankingv2):
    print(f"{k+1}º Lugar para o {v[0]} com o valor {v[1]}")
