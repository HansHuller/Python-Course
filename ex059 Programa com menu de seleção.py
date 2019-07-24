'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação soliciatada em cada passo.

'''
menu = ''
valor1 = ''
valor2 = ''

print("="*60)
while not isinstance(valor1, float):
    valor1 = input("Digite o primeiro valor: ")
    try:
        valor1 = float(valor1)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente!")
while not isinstance(valor2, float):
    valor2 = input("Digite o segundo valor: ")
    try:
        valor2 = float(valor2)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente!")
while menu != 5:
    print("\nSelecione abaixo o que deseja fazer com os valores {:.2f} e {:.2f}:\n"
          "[ 1 ] SOMAR\n"
          "[ 2 ] MULTIPLICAR\n"
          "[ 3 ] MAIOR\n"
          "[ 4 ] NOVOS NÚMEROS\n"
          "[ 5 ] SAIR DO PROGRAMA".format(valor1, valor2))
    try:
        menu = int(input("Qual sua opção? "))
    except ValueError:
        menu = 0
    if menu < 1 or menu >5:
        print("Você selecionou uma opção inválida, tente novamente!")
    elif menu == 1:
        print("A SOMA de {} e {} é: {}".format(valor1, valor2, valor1 + valor2))
    elif menu == 2:
        print("A MULTIPLICAÇÃO de {} e {} é: {}".format(valor1, valor2, valor1 * valor2))
    elif menu == 3:
        print("O MAIOR número entre {} e {} é: {}".format(valor1, valor2, sorted([valor1, valor2])[-1]))
    elif menu == 4:
        valor1 = valor2 = 0
        while not isinstance(valor1, float):
            valor1 = input("Digite o primeiro novo valor: ")
            try:
                valor1 = float(valor1)
                break
            except ValueError:
                print("Você digitou um valor inválido, tente novamente!")
        while not isinstance(valor2, float):
            valor2 = input("Digite o segundo novo valor: ")
            try:
                valor2 = float(valor2)
                break
            except ValueError:
                print("Você digitou um valor inválido, tente novamente!")
    elif menu == 5:
        print("Obrigado por usar nosso serviço!\nAté breve!")
