# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input("Digite um número: "))
print("O dobro de {} é: {:=^10}\nO triplo de {} é: {:=^10}\nA raiz quadrada de {} é {:=^10.4f}".format(n1, n1*2,n1, n1*3, n1, n1**(1/2)))
