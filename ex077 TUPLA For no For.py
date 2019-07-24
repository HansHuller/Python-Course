"""
Crie um programa que tenha uma tupla com várias palavras (Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ("toda", "vez", "que", "eu", "chego", "em", "casa", "a", "barata", "da",
            "vizinha", "esta", "na", "minha", "cama")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for l in p:
        if l.upper() in "AEIOU":
            print(f"{l.lower()} ", end="")
