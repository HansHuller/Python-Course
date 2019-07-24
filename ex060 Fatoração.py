'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
num = ''
fatorial = 1
while not isinstance(num, int):
    num = input("Digite o número que deseja fatorar: ")
    try:
        num = int(num)
        break
    except ValueError:
        print("Você digitou um valor inválido, digite um número inteiro!")
i = num
print("Calculando o {}! = {}".format(num, num), end="")
while not i == 0:
    fatorial *= i
    i -= 1
    print(" x {}".format(i) if i > 0 else " = {}".format(fatorial), end="")

from math import factorial
print("\n{}".format(factorial(num)))
