'''
Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
Exibir sorteados, mostrar resultados de maior e menor
'''
from random import randint
tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(tupla)
print("-="*35)
print("Os números sorteados foram: ", end="")
for n in tupla:
    print(f"{n:^7}", end="")
print("\n", end="")
print("-="*35)
print(f"O maior número sorteado foi:{max(tupla)}")
print("-="*35)
print(f"O menor número sorteado foi:{min(tupla)}")
