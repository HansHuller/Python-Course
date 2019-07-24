'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = 'x'
while sexo not in "MF":                                          #sexo != "M" and sexo != "F":
    sexo = str(input("Digite seu sexo: [M/F]")).upper().strip()[0]
    if sexo not in "MF":                                         #sexo != "M" and sexo != "F":
        print("{:=^80}".format("Você digitou um valor inválido, tente novamente!"))
        print("\33[0;36m-=\33[m"*40)
if sexo in "M":
    print("Bom dia, Senhor!")
else:
    print("Bom dia, Senhorita!")
