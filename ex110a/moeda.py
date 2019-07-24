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


def resumo(valor=0, aumento=10, reducao=10):
    print("="*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("=" * 30)
    print(f"{'Preço analisado:':<20}{moeda(valor):<}")
    print(f"{'Dobro do preço:':<20}{dobro(valor, True):<}")
    print(f"{'Metade do Preço:':<20}{metade(valor, True):<}")
    print(f"{f'{aumento}% de aumento:':<20}{aumentar(valor, aumento, True):<}")
    print(f"{f'{reducao}% de redução:':<20}{diminuir(valor, reducao, True):<}")
    print("="*30)
