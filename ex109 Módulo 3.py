'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
from ex109a import moeda
p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"Aumentando 10% de {moeda.moeda(p)}, temos {moeda.aumentar(p, 10, True)}")
print(f"Diminuindo 10% de {moeda.moeda(p)}, temos {moeda.diminuir(p, 10, True)}")