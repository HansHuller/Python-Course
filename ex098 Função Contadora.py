'''
Faça um programa que ternha uma função chamada contador(), que receba 3 parâmetros: início, fim e passo e realize a
contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.

Testar inicio maior que fim, passo 0(passar passo de 1 em 1) e negativo(número absoluto do digitado).
'''
from time import sleep


def contador(inicio, fim, passo):
    auxfim = 0
    auxpasso = abs(passo)
    if passo == 0:
        auxpasso = 1
    if inicio > fim:
        auxpasso *= -1
        auxfim = fim - 1
    if inicio <= fim:
        auxfim = fim+1
        passo = abs(passo)
    print(f"Iniciando contagem de {inicio} até {fim} de {passo} em {passo}")
    for i in range(inicio, auxfim, auxpasso):
        sleep(0.25)
        print(i, end=" ", flush=True)
    print()


# programa
print("-=-"*20)
contador(1, 10, 1)
print("-=-"*20)
contador(10, 0, 2)
print("-=-"*20)
print("Agora é sua vez de definir a contagem!!")
inicio = int(input("Início: "))
fim = int(input("Fim:    "))
passo = int(input("Passo:  "))
contador(inicio, fim, passo)
