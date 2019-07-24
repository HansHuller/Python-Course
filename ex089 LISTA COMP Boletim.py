'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
Gerar boletim com número do aluno Nome e Média
Depois perguntal qual nota deseja visualizar, ao selecionar o número do aluno exibir as duas notas.
'''
aluno = []
Alunos = []
while True:
    v = 0
    while not isinstance(v, str):
        v = input("Nome do aluno: ")
        try:
            v = float(v)
            v = int(v)
            print("Nome não pode ser um número, tente novamente.")
        except ValueError:
            v = str(v)
    aluno.append(v)
    for n in range(1, 3):
        while not isinstance(v, float):
            v = input(f"Digite {n}ª nota: ")
            try:
                v = float(v)
                if v > 10:
                    print("Você digitou um valor inválido, tente novamente.")
                    v = " "
            except ValueError:
                print("Você digitou um valor inválido, tente novamente.")
        aluno.append(v)
        v = " "
    aluno.append((aluno[1]+aluno[2])/2)
    Alunos.append(aluno[:])
    aluno.clear()
    while v not in "SN":
        v = input("Deseja cadastrar outro aluno [S/N]?  ").upper().strip()[0]
        if v not in "SN":
            print("Valor inválido, tente novamente.")
    if v == "N":
        break
print("="*70)
print(f"{' Boletim ':=^70}")
print("="*70)
print(f"{'Nº':<5}{'NOME':<35}{'MÉDIA':>30}")
for n, a in enumerate(Alunos):
    print(f"{n:<5}{a[0]:.<60}{a[3]:>5.2f}")
print("="*70)
while True:
    v = " "
    while not isinstance(v, int):
        v = input(f"Mostra notas de qual aluno [Nº ou 999 para parar]? ")
        try:
            v = int(v)
            if v >= len(Alunos) and v != 999:
                print("Você digitou um valor inválido, tente novamente.")
                v = " "
        except ValueError:
            print("Você digitou um valor inválido, tente novamente.")
    if v != 999:
        print(f"As notas de {Alunos[v][0]} são: {Alunos[v][1:3]}")
    else:
        print("FINALIZANDO..."
              "\nVOLTE SEMPRE")
        break