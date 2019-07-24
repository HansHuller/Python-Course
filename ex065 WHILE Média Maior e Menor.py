'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''
resp = "S"
cont = soma = 0
while resp == "S":
    print("=" * 70)
    cont += 1
    n = ''
    resp = "vazia"
    while not isinstance(n, int):
        n = input("Digite o {}º número inteiro: ".format(cont))
        try:
            n = int(n)
        except ValueError:
            print("Você não digitou um número inteiro, tente novamente!")
    soma += n
    if cont == 1:
        menor = maior = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    while resp != "S" and resp != "N":
        print("~" * 70)
        resp = str(input("Você deseja digitar mais valores [S/N]? ")).upper().strip()[0]
        if resp != "S" and resp != "N":
            print("Você selecionou uma opção inválida, tente novamente!")
media = soma / cont
print("="*70, "\nVocê informou um total de {} números.\nA média dos valores informados é: {:.2f}\n"
      "O maior valor informado é: {}\nO menor valor informado é: {}"
      .format(cont, media, maior, menor))
