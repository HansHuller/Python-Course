import ex115module


def listar():
    try:
        file = open("C:\\Users\\hans_\\PycharmProjects\\PythonExercicios\\ex115module\\functionalities\\pessoas.text")
    except Exception:
        print(Exception.__cause__)
        result = "Não há cadastros."
    else:
        result = "Há Cadastros"
    return result


print(listar())
