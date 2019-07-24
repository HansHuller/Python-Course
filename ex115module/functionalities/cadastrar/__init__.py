import ex115module


def cadastrar():
    try:
        file = open("C:\\Users\\hans_\\PycharmProjects\\PythonExercicios\\ex115module\\functionalities\\pessoas.text")
    except Exception:
        file = open("pessoas.text", "w")
        print("Arquivo Criado")
    else:
        print("Já existe arquivo")



cadastrar()
