# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input("Digite o valor em metros: "))
print("Este mesmo valor em centímetros é: {:.0f}cm\nE corresponde à {:.0f}mm milímetros!".format(m*100,m*1000))
