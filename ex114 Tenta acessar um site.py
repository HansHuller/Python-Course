'''
Crie um código em Python que teste se o site Pudim está acessível no computador atual.
'''
import urllib.request

try:
    urllib.request.urlopen("http://www.pudim.com.br",)
except Exception as erro:
    print("Não foi possível acessar o site.")
else:
    print(f"O site foi acessado com sucesso!")
