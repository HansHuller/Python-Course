'''
Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno.+
'''
def area():
    largura = float(input(f"{'Largura (metros): ':<35}"))
    comprimento = float(input(f"{'Comprimento (metros): ':<35}"))
    area = largura * comprimento
    print(f"A área de um terreno de{largura:.2f}m X {comprimento:.2f}m é de: {area:.2f}m²")


#Programa
print("-" * 70)
print(f"{'Controle de Terrenos':^70}")
print("-"*70)
area()