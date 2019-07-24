'''
Crie um programa que vai ler vários números e colocá-los em uma lista.
Depois disso, mostre:
Quantos números foram digitados
A lista de valroes, ordenada de forma decrescente.
Se o valor 5 foi digitado e está ou não na lista ( e em qual posição ele está)
'''
lis = []
while True:
    n = ""
    r = " "
    while not isinstance(n, int):
        n = input("Digite um número: ")
        try:
            n = int(n)
        except ValueError:
            print("Você digitou um valor inválido, tente novamente!")
    lis.append(n)
    while r not in "SN":
        r = input("Você gostaria de continuar [S/N]?  ").strip().upper()[0]
        if r not in "SN":
            print("Você selecionou uma opção inválida, tente novamente!")
    if r in "N":
        break
lis.sort(reverse=True)
print("-="*35)
print(f"No total foram digitados {len(lis)} números.")
print(f"A lista digitada em ordem decrescente é: {lis}")
if lis.count(5) > 1:
    print(f"O valor 5 foi digitado {lis.count(5)} vezes.")
elif lis.count(5) == 1:
    print(f"O valor 5 foi digitado {lis.count(5)} vez.")
else:
    print("O valor 5 não foi digitado.")
