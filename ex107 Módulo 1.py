'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas:
aumentar(), %
diminuir(),%
dobro() e
metade()

Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
from ex107a import moeda
p = float(input("Digite o preço: R$"))
print(f"A metade de R${p} é R${moeda.metade(p)}")
print(f"O dobro de R${p} é R${moeda.dobro(p)}")
print(f"Aumentando 10% de {p}, temos R${moeda.aumentar(p, 10)}")
print(f"Diminuindo 10% de {p}, temos R${moeda.diminuir(p, 10)}")

