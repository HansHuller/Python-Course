def aumentar(valor, taxa=10, formatar=False):
    res = valor * (taxa/100+1)
    return res if not formatar else moeda(res)


def diminuir(valor, taxa=10, formatar=False):
    res = valor * (1-taxa/100)
    return res if not formatar else moeda(res)


def dobro(valor, formatar=False):
    res = valor * 2
    return res if not formatar else moeda(res)


def metade(valor, formatar=False):
    res = valor / 2
    return res if not formatar else moeda(res)

def moeda(valor=0, moeda = "R$"):
    return f"{moeda}{valor:.2f}".replace(".",",")