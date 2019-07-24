# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
cores = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}

tri = {"a": float(input("Digite o tamanho do primeiro lado: ")),
       "b":float(input("Digite o tamanho do segundo lado: ")),
       "c":float(input("Digite o tamanho do terceiro lado: "))}
if (abs(tri["b"] - tri["c"]) < tri["a"] < (tri["b"] + tri["c"])) and (abs(tri["b"] - tri["a"]) < tri["c"] < (tri["b"] + tri["a"])) and (abs(tri["a"] - tri["c"]) < tri["b"] < (tri["a"] + tri["c"])):
    print("Com esses valores de lados, é possível criar um triângulo!")
else:
    print("É impossível criar um triângulo com esses lados!!!")
