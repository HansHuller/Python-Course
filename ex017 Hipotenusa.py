from math import hypot
catetooposto = float(input("Insira o valor do cateto oposto: "))
catetoadjacente = float(input("Insira o valor do cateto adjacente: "))
print("O valor da hipotenusa é: {:.2f} ou {:.2f} ".format(hypot(catetoadjacente, catetooposto), (catetooposto**2 + catetoadjacente**2)**(1/2)))
