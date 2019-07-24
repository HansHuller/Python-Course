# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados por unidade dezena centena e milhar
# tente fazer por matemática e por string

num = str(input("Digite um número entre 0 e 9999: "))
numint = int(num)

print("A unidade é: {}\nA dezena é: {}\nA centena é: {}\nO milhar é: {}".format(num[3], num[2],
                                                                                num[1], num[0]))

print("A unidade é: {}\nA dezena é: {}\nA centena é: {}\nO milhar é: {}".format(numint // 1 % 10, numint // 10 % 10,
                                                                                numint // 100 // 10, numint // 1000 % 10))
#print("{},{}".format(num, numint))