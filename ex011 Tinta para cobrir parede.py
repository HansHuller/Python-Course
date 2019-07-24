# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta nedessária para pintá-la sabendo que cada litro de tinta, pinta uma área de 2m

x = float(input("Digite a altura da parede: "))
y = float(input("Digite a largura da parede: "))
z = x*y/2

print("Sua parede de dimensões de {}m X {}m possue área de {:.2f}m².\n"
      "Para pintar essa parede você precisará de {:.2f} l de tinta!!".format(x, y, x*y, z))
