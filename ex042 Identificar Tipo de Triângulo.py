''' REFAZER DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados são iguais
Isósceles: dois lados iguais
Escaleno: todos os lados são diferentes'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
tri = {"a": float(input("Digite o tamanho do primeiro lado: ")),
       "b":float(input("Digite o tamanho do segundo lado: ")),
       "c":float(input("Digite o tamanho do terceiro lado: "))}
if (abs(tri["b"] - tri["c"]) < tri["a"] < (tri["b"] + tri["c"])) and (abs(tri["b"] - tri["a"]) < tri["c"] < (tri["b"] + tri["a"])) and (abs(tri["a"] - tri["c"]) < tri["b"] < (tri["a"] + tri["c"])):
    print("Com esses valores de lados, é possível criar um triângulo do tipo: ", end="")
    if tri["a"] == tri["b"] == tri["c"]:
        print("EQUILÁTERO!")
    elif tri["a"] == tri["b"] or tri["a"] == tri["c"] or tri["b"] == tri["c"]:
        print("ISÓSCELES!")
    else: # tri["a"] != tri["b"] != tri["c"] != tri["a"]:
        print("Escaleno!")
else:
    print("É impossível criar um triângulo com esses lados!!!")
