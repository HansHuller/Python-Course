'''
Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes de aproveitamento de cada jogador.
mostrar uma tabela (PARECIDA COM BOLETIM) com código do jogador, nome, gols, total de gols e pedir código para exibir
quantos gols o jogador fez em cada jogo.
'''
lisJog = []
jogador = {}
while True:
    opcao = nome = int()
    partidas = str()
    gols = []
    while not isinstance(nome, str):
        nome = input(f"{'Nome do jogador: ':<30}")
        try:
            nome = float(nome)
            nome = int(nome)
            print(f"Nome não pode ser um número! Tente novamente...")
        except ValueError:
            nome = str(nome)
    jogador["nome"] = nome
    while not isinstance(partidas, int):
        partidas = input(f"{'Partidas jogadas: ':<30}")
        try:
            partidas = int(partidas)
            if partidas == 0:
                partidas = " "
                print(f"O jogador precisa ter jogado alguma partida!")
        except ValueError:
            print("Número de partidas precisa ser um número! Tente novamente...")
    for p in range(0, partidas):
        gol = " "
        while not isinstance(gol, int):
            gol = input(f"Gols marcados na {p+1}ª partida:  ")
            try:
                gol = int(gol)
            except ValueError:
                print("Número de gols precisa ser um número! Tente novamente...")
        gols.append(gol)
    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    lisJog.append(jogador.copy())
    jogador.clear()

    while not isinstance(opcao, str):
        opcao = input(f"{'Deseja continuar [S/N]? ':<30}")
        try:
            opcao = float(opcao)
            opcao = int(opcao)
            print(f"Não pode escolher um número! Tente novamente...")
        except ValueError:
            opcao = str(opcao).upper().strip()[0]
            if opcao not in "SN":
                print("Você digitou uma opcao inválida! Tente novamente...")
                opcao = 0
    if opcao == "N":
        break
print("="*70)
print()
print("="*70)
print(f"{' Jogadores ':=^70}")
print("="*70)
print(f"{'cod':<5}",end='')
for k in lisJog[0].keys():
    print(f"{k.capitalize():<30}", end='')
print()
print("-"*70)
for c, i in enumerate(lisJog):
    print(f"{c:<5}", end='')
    for v in i.values():
        print(f"{str(v):<30}", end="")
    print()
while True:
    opcao = " "
    while not isinstance(opcao, int):
        opcao = input("Deseja saber os detalhes de qual jogador? [Digite 999 para sair]  ")
        try:
            opcao = int(opcao)
            if opcao > (len(lisJog) - 1) and opcao != 999:
                opcao = " "
                print("Você uma opção inválida, tente novamente!")
        except ValueError:
            print("Você uma opção inválida, tente novamente!")
    if opcao == 999:
        break
    print(f" - - Levantando dados do jogador {lisJog[opcao]['nome']}:")
    for p, g in enumerate(lisJog[opcao]['gols']):
        print(f"     Na {p+1}ª partida, marcou {g} gols.")
print(f"{'PROGRAMA ENCERRADO':-^70}")
