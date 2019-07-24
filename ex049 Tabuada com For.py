'''
Refaça o exercício da tabuada (009) mostrando a tabuada de um número que o usuário escolher, so que usando laço FOR
'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
num = int(input("Digite o número cuja tabuada você deseja: "))
tab = int(input("Digite até qual múltiplicador deseja calcular: "))
print("-"*20)
for i in range(1, tab+1):
    print("{:>3}{:>3}{:>3}{:>3}{:>7}".format(num, "*", i, "=", num * i))
print("-"*20)

for i in range(0, num*tab+1, num):
    print("{:>3}{:>3}{:>3}{:>3}{:>7}".format(num, "*", i, "=", i))
print("-" * 20)

