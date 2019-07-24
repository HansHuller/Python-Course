def titulo(frase):
    print("-" * 70)
    print(f"{frase.upper():^70}")
    print("-" * 70)


def texto(frase):
    print(f"{frase.upper():<40}")


def choose(text="Qual sua opção? ", errormsg="Sua opção é inválida! Tente novamente!"):
    choice = " "
    while not isinstance(choice, int):
        choice = input(f"{text:<40}")
        try:
            choice = int(choice)
        except:
            print(f"{errormsg}")
        else:
            if not (0 < choice < 4):
                choice = " "
                print(f"{errormsg}")
    return choice


