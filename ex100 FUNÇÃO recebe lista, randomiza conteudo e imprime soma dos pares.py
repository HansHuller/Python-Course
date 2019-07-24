'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira vai sortear 5 números e colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
'''
from random import randint


def sorteia(lista):
    aux = int()
    print("Sorteando 5 valores para a lista: ", end="")
    for i in range(0, 5):
        aux = randint(0, 10)
        print(f"{aux}", end=" ")
        lista.append(aux)
    print()
def somaPar(lista):
    soma = int()
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"Somando os valores pares de {lista}, temos o resultado: {soma}")


# Programa
lista = list()
sorteia(lista)
somaPar(lista)
