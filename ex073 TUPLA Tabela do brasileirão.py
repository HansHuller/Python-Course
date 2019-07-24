'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
Apenas os 5 primeiros colocados
Os últimos 4 colocados da tabela.
Uma lista com os times em ordem alfabética.
Em que posição está o time da Chapecoense

(Listar times no começo)
'''
brasileiro = ("Palmeiras", "Santos", "Atlético Mineiro", "Botafogo", "Flamengo", "Bahia", "Internacional",
               "São Paulo", "Goiás", "Corinthians", "Atlético-PR", "Ceará", "Grêmio", "Cruzeiro", "Fluminense",
               "Chapecoense", "Fortaleza", "Vasco da Gama", "CSA", "Avaí")
for cont, n in enumerate(brasileiro):
    print(f"{cont+1:>3}o colocado: {n}")
print("-"*70)
print("Os 5 primeiros colocados são:")
for n in range(0, 5):
    print(f"{n+1:>3}o colocado: {brasileiro[n]}")
print("-"*70)
print("Os 4 últimos colocados são:")
for n in range(len(brasileiro)-4, len(brasileiro)):
    print(f"{n+1:>3}o colocado: {brasileiro[n]}")
print("-"*70)
print(f"A lista de times em ordem alfabética é: {sorted(brasileiro)}")
print("-"*70)
print(f"O time da Chapecoense, VIVA CHAPE!!, está na {brasileiro.index('Chapecoense')+1}a posição")
