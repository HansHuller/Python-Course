'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de fibonacci.
0 > 1 > 1 > 2 > 3 > 5 > 8
'''
n = ''
i = 1
n1 = 0
n2 = 1
n3 = 0

print("{:-^70}".format("Sequencia de Fibonacci"))

while not isinstance(n, int):
    n = input("Digite quantos termos da sequência de Fibonacci deseja visualizar: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente!")
while i <= n:
    if i == 1:
        print("~" * 70)
    print("{} → ".format(n1), end="")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    i += 1
print("FIM!")
print("~"*70)
