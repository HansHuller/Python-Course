'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular
ex lista = ("Pão", 1, "Leite", 3.50) Exibir lista como se fosse nota fiscal, com pontos separando o valor e o produto.
'''
lista = ("Pão", 1.00, "Leite", 3.50, "Camiseta", 49.99, "Calça", 299.50, "Chinelo", 39.49, "Meia", 9.20
         , "Mochila", 100, "Tupperware", 40, "Marmitas", 460)
soma = 0
print("-"*70)
print(f"{'LISTA DE ITENS':^70}")
print("-"*70)
for i in range(0, len(lista), 2):
    print(f"{lista[i]:.<62}R${lista[i+1]:>6.2f}")
    soma += lista[i+1]
print("="*70)
print(f"{'Total':.<60}R${soma:>8.2f}")
