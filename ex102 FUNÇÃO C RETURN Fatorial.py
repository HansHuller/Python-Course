'''
Crie um programa qeu tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial.
construir docstring
'''
def fatorial(num, show = False):
    """
    Programa que calcula fatorial do número informado
    :param num: Número utilizado para calcular o fatorial
    :param show: OPCIONAL padrão = FALSE. Parâmetro define se o processo de cálculo sera exibido
    :return: Fatorial do número informado
    """
    fat = 1
    cont = num
    if show == False:
        while cont > 0:
            fat *= cont
            cont -= 1
        return fat
    else:
        texto = f"Calculando fatorial de {num}: {num}"
        while cont > 0:
            fat *= cont
            texto = (texto + f" x {cont}")
            cont -= 1
        texto = (texto + f" = {fat}")
        return texto

print(fatorial(5))
print(fatorial(5, show=True))

