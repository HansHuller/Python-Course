def aumentar(valor, taxa=10):
    res = valor * (taxa/100+1)
    return res


def diminuir(valor, taxa=10):
    res = valor * (1-taxa/100)
    return res


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2

def moeda(valor=0, moeda = "R$"):
    return f"{moeda}{valor:.2f}".replace(".",",")