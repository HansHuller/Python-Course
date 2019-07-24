'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
Exibir a quantidade de jogos que o jogador X jogou, a quantidade de gols em cada partida e o total de gols.
'''
jogador = {}
gols = []
nome = int()
partidas = str()
while not isinstance(nome, str):
    nome = input(f"{'Nome do jogador: ':<15}")
    try:
        nome = float(nome)
        nome = int(nome)
        print(f"Nome não pode ser um número! Tente novamente...")
    except ValueError:
        nome = str(nome)
jogador["nome"] = nome
while not isinstance(partidas, int):
    partidas = input(f"{'Partidas jogadas: ':<15}")
    try:
        partidas = int(partidas)
        if partidas == 0:
            partidas = " "
            print(f"O jogador precisa ter jogado alguma partida!")
    except ValueError:
        print("Número de partidas precisa ser um número! Tente novamente...")
jogador["partidas"] = partidas
for p in range(0, jogador["partidas"]):
    gol = " "
    while not isinstance(gol, int):
        gol = input(f"Gols marcados na {p+1}ª partida: ")
        try:
            gol = int(gol)
        except ValueError:
            print("Número de gols precisa ser um número! Tente novamente...")
    gols.append(gol)
jogador["gols"] = gols[:]
jogador["total"] = sum(gols)
print("-=-"*22)
print(jogador)
print("-=-"*22)
for k, v in jogador.items():
    print(f"O campo {k.capitalize()} tem o valor {v}")
print("-=-"*22)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} paridas. ")
for n, i in enumerate(jogador["gols"]):
    print(f"Na {n+1}ª partida, {jogador['nome']} marcou {i} gols.")
print(f"{jogador['nome']} marcou ao todo {jogador['total']} gols.")
