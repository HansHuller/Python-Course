'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menos nota
- A média da turma
- A situação (opcional) [média > 7 = BOA, >5 = RAZOAVEL, <5 = ruim]
Fazer DOCSTRINGS
'''


def notas(*notas, sit = False):
    """
    Função para analisar notas de alunos
    :param notas: uma ou mais notas de alunos
    :param sit: valor opcional, indica se deve ou não adicionar situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    result = dict()
    result["total"] = len(notas)
    result["maior"] = max(notas)
    result["menor"] = min(notas)
    result["média"] = sum(notas)/len(notas)
    if sit:
        if result["média"] >= 7:
            result["situação"] = "BOA"
        elif result["média"] >= 5:
            result["situação"] = "RAZOÁVEL"
        else:
            result["situação"] = "RUIM"
    return result


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
