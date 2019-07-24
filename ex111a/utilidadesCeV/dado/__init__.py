def inputMoney(texto="Digite um valor: R$"):
    dinheiro = str()
    teste = 0
    while not isinstance(dinheiro, float):
        dinheiro = input(f"{texto}").replace(",",".").strip()
        try:
            dinheiro = float(dinheiro)
        except ValueError:
            if dinheiro == "":
                print(f"\033[0;31mERRO '' é um valor inválido!\033[m")
            else:
                print(f"\033[0;31mERRO {dinheiro} é um valor inválido!\033[m")
    return dinheiro


def inputInt(frase = "Digite um número inteiro: ", nomeVar = "Variável"):
    aux = " "
    while not isinstance(aux, int):
        aux = input(f"{frase:<30}")
        if aux == "":
            aux = 0
        try:
            aux = int(aux)
        except ValueError:
            print(f"\033[1;31m{nomeVar.upper()}\033[m \033[0;31mprecisa ser um número inteiro! Tente novamente...\033[m")
    return aux


def inputFloat(frase = "Digite um número real: ", nomeVar = "Variável"):
    aux = " "
    while not isinstance(aux, float):
        aux = input(f"{frase:<30}").replace(",", ".")
        if aux == "":
            aux = 0
        try:
            aux = float(aux)
        except ValueError:
            print(f"\033[1;31m{nomeVar.upper()}\033[m \033[0;31mprecisa ser um número real! Tente novamente...\033[m")
    return aux


