'''
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
Quantas vezes apareceu o valor 9.
Em que posição foi digitado o primeiro valor 3.
Quais foram os números pares
'''
a = b = c = d =''
while not isinstance(a, int):
    a = input("Digite um número inteiro: ")
    try:
        a = int(a)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente!")
while not isinstance(b, int):
    b = input("Digite um número inteiro: ")
    try:
        b = int(b)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente!")
while not isinstance(c, int):
    c = input("Digite um número inteiro: ")
    try:
        c = int(c)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente!")
while not isinstance(d, int):
    d = input("Digite um número inteiro: ")
    try:
        d = int(d)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente!")
tupla = (a, b, c, d)
print(f"O valor 9 apareceu {tupla.count(9)} vezes.")
if 3 in tupla:
    print(f"O número 3 foi digitado na {tupla.index(3)+1}a posição pela primeira vez.")
else:
    print(f"O número 3 não foi digitado.")
print(f"Os números pares digitados são: ", end="")
for i in tupla:
    if i % 2 == 0:
        print(f"{i} ", end="")

'''while True:
    n = ''
    tup = ()
    while not isinstance(n, int):
        n = input("Digite um número inteiro: ")
        try:
            n = int(n)
            break
        except ValueError:
            print("Você digitou um valor inválido, tente novamente!")
    tup = tupla + tuple(n)
    tupla = tup
    if len(tupla) >= 4:
        break
print(tupla)'''