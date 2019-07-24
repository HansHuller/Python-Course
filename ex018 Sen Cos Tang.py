#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
from math import radians, sin, cos, tan, degrees
ang = (radians(float(input("Digite o ângulo: "))))
print("Para o ângulo de {:.2f} graus seu seno é: {:.2f}\nSeu cosseno é: {:.2f}\n E sua tangente é: {:.2f}".format(degrees(ang),sin(ang),cos(ang),tan(ang)))
