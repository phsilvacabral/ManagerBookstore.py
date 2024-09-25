from time import sleep
import Livros
import Alunos
import pickle
import Livros2
from utilidades import cor


def menu_princ():
    msg = "          Gerenciamento de Biblioteca          "
    print(cor(len(msg) * " ", 1, 30, 107))
    print(msg)
    print(len(msg) * " ")
    print(f"{cor(' 1 ', 1, 97, 104, True)}{cor('➔ Módulo de Empréstimo de Livros', 1, 97, 47)}")
    print(f"{cor(' 2 ', 1, 97, 102, True)}{cor('➔ Módulo de Estoque de Livros', 1, 97, 47)}")
    print(f"{cor(' 3 ', 1, 97, 103, True)}{cor('➔ Módulo de Registro de Alunos', 1, 97, 47)}")
    print(cor(' 4 🡠 Sair', 7, 37, 107))
    print(60 * "‗‗")
    return int(input(cor(" Digite sua opção: ")))


def start(database: dict):
    while True:
        try:
            op = menu_princ()
            if op == 1:
                sleep(0.5)
                Livros2.start(database)
            elif op == 2:
                sleep(0.5)
                Livros.start(database)
            elif op == 3:
                sleep(0.5)
                Alunos.start(database)
            elif op == 4:
                sleep(0.5)
                return
            else:
                print(cor(" ✘ Opção inválida!", 1, 0, 1, True))
                sleep(0.5)
        except ValueError:
            print(cor(" ✘ Entrada inválida. Por favor, digite um número válido!", 1, 31, 1, True))
            sleep(0.5)
            continue


if __name__ == '__main__':
    database = {
        "alunos": {

        },
        "livros_livres": {},
        "livros_emprestados": {}
    }
    try:
        with open("livros_dict.pkl", "rb") as f:
            database = pickle.load(f)
    except FileNotFoundError:
        print(cor(" ✘ Arquivo 'livros_dict.pkl' não encontrado. Um novo arquivo será criado!", 1, 31, 1, True))
    start(database)
    with open("livros_dict.pkl", "wb") as f:
        pickle.dump(database, f)
    print(cor("""                  
                Obrigado por usar o sistema!!!
     """, 1, 30, 107))
