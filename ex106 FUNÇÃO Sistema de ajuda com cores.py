'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. quan o usuário digitar a palavra "FIM", o programa se encerrará.
USE CORES!
'''


def escreva(frase):
    frase = "  " + frase + "  "
    tam = len(frase)
    print("~" * tam)
    print(f"{frase}")
    print("~" * tam)

def ajuda():
    from time import sleep
    while True:
        print("\033[1;30;46m", end="")
        escreva("SITEMA DE AJUDA HELLpy")
        print("\033[m", end="")
        print()
        opcao = input("Digite o nome da FUNÇÃO ou BIBLIOTECA que deseja consultar > ")
        if opcao.upper() == "FIM":
            break
        print()
        print("\033[1;30;44m", end="")
        escreva(f"Consultando o manual de '{opcao}'")
        sleep(0.5)
        print("\033[m", end="")
        print()
        print("\033[7;30;49m", end="")
        help(opcao)
        print("\033[m", end="")
        print()
    escreva("<<<<<<<<PROGRAMA FINALIZADO>>>>>>>>")

ajuda()
