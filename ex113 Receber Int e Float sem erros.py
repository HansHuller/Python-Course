'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
Se o usuário não digitar entra o valor 0.
'''

from ex111a.utilidadesCeV import dado

inteiro = dado.inputInt()
real = dado.inputFloat()

print(f"Número inteiro: {inteiro}\nNúmero real: {real}")
