from time import sleep
from utilidades import cor


def entrada_l_n(livros_livres, livros_emprestados):
    while True:
        livro_escolhido = input("Digite o nome do livro: ").lower()
        while livro_escolhido.strip() == "":
            print(cor("✘ Livro inválido!", 1, 31, 1, True))
            livro_escolhido = input("Digite o nome do livro: ").lower()
        while True:
            try:
                quant = int(input("Qual a quantidade a ser registrada: "))
                if quant <= 0:
                    print(cor("✘ A quantidade deve ser um número inteiro positivo!", 1, 31, 1, True))
                else:
                    break
            except ValueError:
                print(cor("✘ Entrada inválida. Por favor, digite um número inteiro válido!", 1, 31, 1, True))
        if livro_escolhido in livros_livres:
            print(cor('✘ Esse livro já está cadastrado no estoque!', 1, 31, 1, True))
            print(f'Existem '
                  f'{livros_livres[livro_escolhido]["quantidade"] + livros_emprestados[livro_escolhido]["quantidade"]} '
                  f'deste livro no estoque')
            livros_livres[livro_escolhido]['quantidade'] += quant
            print(f'Novo total: '
                  f'{livros_livres[livro_escolhido]["quantidade"] + livros_emprestados[livro_escolhido]["quantidade"]}')
            print(cor('✔ Quantidade alterada!', 1, 32, 1, True))
        else:
            print(cor("✔ Esse livro foi cadastrado ao estoque!", 1, 32, 1, True))
            livros_livres[livro_escolhido] = {"quantidade": quant}
            livros_emprestados[livro_escolhido] = {"quantidade": 0}
        sair = False
        while True:
            i = input('Continuar adicionando? (s/n) ➔ ').lower()
            while i.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                i = input('Continuar adicionando? (s/n) ➔ ').lower()
            if i in {"s", "sim"}:
                break
            elif i in {"n", "não", "nao"}:
                sair = True
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
        if sair:
            break
    sleep(0.5)


def saida_l_a(livros_livres, livros_emprestados):
    if livros_emprestados == {} and livros_livres == {}:
        print(cor('✘ Não tem nenhum livro cadastrado no sistema!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                entrada_l_n(livros_livres, livros_emprestados)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    else:
        while True:
            livro_retirar = input("Digite o nome do livro para descadastrar: ").lower()
            while livro_retirar.strip() == "":
                print(cor("✘ Livro inválido!", 1, 31, 1, True))
                livro_retirar = input("Digite o nome do livro para descadastrar: ").lower()
            if livro_retirar not in livros_livres:
                print(cor(f'✘ O livro {livro_retirar} não está cadastrado!', 1, 31, 1, True))
            elif livros_emprestados[livro_retirar]['quantidade'] > 0:
                print(f'Existe {livros_emprestados[livro_retirar]["quantidade"]} deste livro em empréstimo.')
                print(cor('✘ Não é possível apagar o livro até todos estiverem disponíveis!', 1, 31, 1, True))
            elif livro_retirar in livros_livres:
                print(f'Existe {livros_livres[livro_retirar]["quantidade"]} deste livro no estoque.')
                while True:
                    try:
                        quant = int(input("Digite a quantidade a ser descadastrada: "))
                        if quant <= 0:
                            print(cor("✘ A quantidade deve ser um número inteiro positivo!", 1, 31, 1, True))
                        elif quant > livros_livres[livro_retirar]["quantidade"]:
                            print(cor("✘ A quantidade inserida é maior que a atual no estoque!", 1, 31, 1, True))
                        else:
                            break
                    except ValueError:
                        print(cor("✘ Entrada inválida. Por favor, digite um número inteiro válido!", 1, 31, 1, True))
                livros_livres[livro_retirar]['quantidade'] -= quant
                print(cor(f"✔ Foram descadastrado {quant} unidades do livro {livro_retirar}!", 1, 32, 1, True))
                if livros_livres[livro_retirar]['quantidade'] <= 0:
                    del livros_livres[livro_retirar]
                    print(cor("✔ Livro descadastrado permanentemente!", 1, 32, 1, True))
                    if livros_emprestados[livro_retirar]['quantidade'] <= 0:
                        del livros_emprestados[livro_retirar]
            else:
                print(cor("✘ O livro não existe no estoque!", 1, 31, 1, True))
            sair = False
            while True:
                i = input('Continuar removendo? (s/n) ➔ ').lower()
                while i.strip() == "":
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
                    i = input('Continuar removendo? (s/n) ➔ ').lower()
                if i in {"s", "sim"}:
                    break
                elif i in {"n", "não", "nao"}:
                    sair = True
                    break
                else:
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
            if sair:
                break
    sleep(0.5)


def pesquisar_l(alunos, livros_livres, livros_emprestados):
    if livros_emprestados == {} and livros_livres == {}:
        print(cor('✘ Não tem nenhum livro cadastrado no estoque!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                entrada_l_n(livros_livres, livros_emprestados)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    else:
        while True:
            livro = input('Digite o nome do livro que deseja pesquisar: ').lower()
            while livro.strip() == "":
                print(cor("✘ Livro inválido!", 1, 31, 1, True))
                livro = input('Digite o nome do livro que deseja pesquisar: ').lower()
            if livro not in livros_livres:
                print(cor("✘ Livro inválido!", 1, 31, 1, True))
                while True:
                    resp = input('Deseja cadastrar o livro? (s/n) ➔ ').lower()
                    while resp.strip() == "":
                        print(cor('✘ Valor inválido!', 1, 31, 1, True))
                        resp = input('Deseja cadastrar o livro? (s/n) ➔ ').lower()
                    if resp in {"s", "sim"}:
                        entrada_l_n(livros_livres, livros_emprestados)
                        break
                    elif resp in {"n", "não", "nao"}:
                        break
                    else:
                        print(cor('✘ Valor inválido!', 1, 31, 1, True))
            elif livro in livros_livres:
                print(f"O Livro {livro} tem {livros_livres[livro]['quantidade']} disponíveis.")
                print(f"O Livro: {livro} tem {livros_emprestados[livro]['quantidade']} em empréstimo.")
                print(f'Total: {livros_livres[livro]["quantidade"] + livros_emprestados[livro]["quantidade"]}')
                livro_presente = False
                for aluno_cpf, aluno_info in alunos.items():
                    if 'livro' in aluno_info and livro in aluno_info['livro']:
                        livro_presente = True
                        print(cor(f" Aluno: {aluno_info['nome']} - ({aluno_info['livro']}) - "
                                  f"({aluno_info['saida']} - CPF: {aluno_cpf}) ", 1, 30, 102, True))
                if not livro_presente:
                    print(cor("✘ Nenhum aluno possui esse livro!", 1, 31, 1, True))
            sair = False
            while True:
                i = input('Continuar pesquisando? (s/n) ➔ ').lower()
                while i.strip() == "":
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
                    i = input('Continuar pesquisando? (s/n) ➔ ').lower()
                if i in {"s", "sim"}:
                    break
                elif i in {"n", "não", "nao"}:
                    sair = True
                    break
                else:
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
            if sair:
                break
    sleep(0.5)


def listar_l(livros_livres, livros_emprestados):
    if livros_emprestados == {} and livros_livres == {}:
        print(cor('✘ Não tem nenhum livro cadastrado no estoque!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                entrada_l_n(livros_livres, livros_emprestados)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    else:
        while True:
            try:
                msg = "     Listagem de Livros     "
                print(cor(len(msg) * " ", 1, 30, 102))
                print(msg)
                print(len(msg) * " ")
                print(cor(" 1 ➔ Livros Disponiveis", 1, 92, 100))
                print(" 2 ➔ Livros em Empréstimo")
                print(" 3 ➔ Todos os Livros")
                print(" 4 🡠 Voltar")
                print(len(msg) * "‗‗")
                op = int(input(cor(" Digite sua opção: ")))
                if op == 1:
                    if not any(v['quantidade'] >= 1 for v in livros_livres.values()):
                        print(cor('✘ Nenhum livro está disponível no momento!', 1, 31, 1, True))
                    else:
                        for k, v in livros_livres.items():
                            print(f"Livro Disponível: {k:<35} ⎢ Quantidade: {v['quantidade']}")
                    sleep(0.5)
                if op == 2:
                    if not any(v['quantidade'] >= 1 for v in livros_emprestados.values()):
                        print(cor('✘ Nenhum livro está sendo emprestado no momento!', 1, 31, 1, True))
                    else:
                        for k, v in livros_emprestados.items():
                            if v['quantidade'] >= 1:
                                print(f"Livro em Empréstimo: {k:<35} ⎢ Quantidade: {v['quantidade']}")
                    sleep(0.5)
                if op == 3:
                    if not any(v['quantidade'] >= 1 for v in livros_livres.values()):
                        print(cor('✘ Nenhum livro está disponível no momento!', 1, 31, 1, True))
                    else:
                        for k, v in livros_livres.items():
                            print(f"Livro Disponível: {k:<35} ⎢ Quantidade: {v['quantidade']}")
                    if not any(v['quantidade'] >= 1 for v in livros_emprestados.values()):
                        print(cor('✘ Nenhum livro está sendo emprestado no momento!', 1, 31, 1, True))
                    else:
                        for k, v in livros_emprestados.items():
                            if v['quantidade'] >= 1:
                                print(f"Livro em Empréstimo: {k:<35} ⎢ Quantidade: {v['quantidade']}")
                    sleep(0.5)
                if op == 4:
                    break
                elif op != 1 and op != 2 and op != 3 and op != 4:
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
            except ValueError:
                print(cor("✘ Entrada inválida. Por favor, digite um número válido!", 1, 31, 1, True))
    sleep(0.5)


def menu():
    msg = "          Módulo de Estoque de Livros          "
    print(cor(len(msg) * " ", 1, 30, 102))
    print(msg)
    print(len(msg) * " ")
    print(cor(" 1 ➔ Cadastramento de Livros", 7, 36, 90))
    print(" 2 ➔ Descadastramento de Livros")
    print(" 3 ➔ Pesquisa de Livros")
    print(" 4 ➔ Listagem de Livros")
    print(" 5 🡠 Voltar")
    print(60 * "‗‗")
    return int(input(cor(" Digite sua opção: ")))


def start(database):
    while True:
        try:
            op = menu()
            if op == 1:
                sleep(0.5)
                entrada_l_n(database["livros_livres"], database['livros_emprestados'])
            elif op == 2:
                sleep(0.5)
                saida_l_a(database["livros_livres"], database["livros_emprestados"])
            elif op == 3:
                sleep(0.5)
                pesquisar_l(database['alunos'], database["livros_livres"], database["livros_emprestados"])
            elif op == 4:
                sleep(0.5)
                listar_l(database["livros_livres"], database["livros_emprestados"])
            elif op == 5:
                sleep(0.5)
                return
            else:
                print(cor(" ✘ Opção inválida!", 1, 31, 1, True))
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
    start(database)
