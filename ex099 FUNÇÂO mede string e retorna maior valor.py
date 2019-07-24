'''
Faça um programa que tenha uma função maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e retornar qual deles é o maior.
'''
def maior(*numeros):
    print("=-="*20)
    print("Analisando os valores passados...")
    '''cont = 0
    while cont < len(numeros):
        print(numeros[cont], end=" ")
        cont +=1'''
    for i in numeros:
        print(i, end=" ")
    if len(numeros) == 0:
        maior = 0
    else:
        maior = max(numeros)
    print()
    print(f"O total de valores informados é: {len(numeros)}.")
    print(f"O maior valor informado foi: {maior}.")


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()