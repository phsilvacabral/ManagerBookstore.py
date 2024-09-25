from time import sleep
import re
import Verificadores
from utilidades import cor


def adicionar_a(alunos):
    nome = input('Digite o nome do aluno: ')
    while nome.strip() == "":
        print(cor("✘ Nome inválido!", 1, 31, 31, True))
        nome = input('Digite o nome do aluno: ')
    numero = input("Digite o número de telefone com DDD sem o zero: ")
    while not Verificadores.verificar_n_t(numero):
        print(cor("✘ Número de telefone inválido!", 1, 31, 1, True))
        numero = input("Digite o número de telefone DDD sem o zero: ")
    cpf = input("Digite o CPF: ")
    while not Verificadores.verificar_cpf(cpf):
        print(cor("✘ CPF inválido!", 1, 31, 1, True))
        cpf = input("Digite o CPF: ")
    cpf = re.sub(r'\D', '', cpf)
    cpf_f = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
    numero = re.sub(r'\D', '', numero)
    numero_f = re.sub(r'(\d{2})(\d{4,5})(\d{4})', r'(\1) \2-\3', numero)
    if not (cpf_f in alunos):
        alunos[cpf_f] = {'nome': nome, 'telefone': numero_f}
        print(cor('✔ Aluno registrado!', 1, 32, 1, True))
    else:
        while True:
            resp = input(f'{cor("✘ Este CPF já existe.", 1, 31, 1, True)} Gostaria de Editar? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input(f'{cor("✘ Este CPF já existe.", 1, 31, 1, True)} Gostaria de Editar? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                editar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    sleep(0.5)


def apagar_a(alunos):
    if alunos == {}:
        print(cor('✘ Não tem alunos cadastrados no sistema!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                adicionar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    else:
        cpf = input('Informe o CPF do aluno para o descadastramento: ')
        while not Verificadores.verificar_cpf(cpf):
            print(cor("✘ CPF inválido!", 1, 31, 1, True))
            cpf = input('Informe o CPF do aluno para o descadastramento: ')
        cpf = re.sub(r'\D', '', cpf)
        cpf_f = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
        if cpf_f in alunos:
            if "livro" in alunos[cpf_f]:
                print(cor('✘ Não é possível descadastrar o aluno com livro em empréstimo!', 1, 31, 1, True))
            else:
                print(cor(f'✔ O aluno {alunos[cpf_f]["nome"]} com CPF {cpf_f} '
                          f'foi descadastrado do sistema!', 1, 32, 1, True))
                del alunos[cpf_f]
        else:
            print(cor('✘ CPF não cadastrado.', 1, 31, 1, True))
    sleep(0.5)


def editar_a(alunos):
    if alunos == {}:
        print(cor('✘ Não tem alunos cadastrados no sistema.', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                adicionar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    else:
        cpf = input('Informe o CPF do aluno para a edição: ')
        while not Verificadores.verificar_cpf(cpf):
            print(cor('✘ CPF inválido!', 1, 31, 1, True))
            cpf = input('Informe o CPF do aluno para a edição: ')
        cpf = re.sub(r'\D', '', cpf)
        cpf_f = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
        if cpf_f in alunos:
            aluno = alunos[cpf_f]
            print(cor(f" Aluno: {aluno['nome']} - Telefone: {aluno['telefone']} - CPF: {cpf_f} ", 1, 30, 103, True))
            print('Edições possíveis: Nome, Telefone, CPF.')
            while True:
                edit = input('Informe qual é a edição: ').lower()
                while edit.strip() == "":
                    print(cor("✘ Entrada inválida!", 1, 31, 1, True))
                    edit = input('Informe qual é a edição: ').lower()
                if edit in {'nome', 'telefone', 'cpf'}:
                    if edit in {'nome'}:
                        edits = input('Informe a mudança: ')
                        while edits.strip() == "":
                            print(cor("✘ Entrada inválida!", 1, 31, 1, True))
                            edits = input('Informe a mudança: ')
                        alunos[cpf_f].update({"nome": edits})
                        print(cor('✔ Alteração Feita!', 1, 32, 1, True))
                        break
                    elif edit in {'telefone'}:
                        edits = input('Informe a mudança: ')
                        while not Verificadores.verificar_n_t(edits):
                            print(cor("✘ Número de telefone inválido!", 1, 31, 1, True))
                            edits = input('Informe a mudança: ')
                        edits_f = re.sub(r'\D', '', edits)
                        edits_f_f = re.sub(r'(\d{2})(\d{4,5})(\d{4})', r'(\1) \2-\3', edits_f)
                        alunos[cpf_f].update({"telefone": edits_f_f})
                        print(cor('✔ Alteração Feita!', 1, 32, 1, True))
                        break
                    elif edit in {'cpf'}:
                        edits = input('Informe a mudança: ')
                        while not Verificadores.verificar_cpf(edits):
                            print(cor("✘ CPF inválido!", 1, 31, 1, True))
                            edits = input('Informe a mudança: ')
                        edits_f = re.sub(r'\D', '', edits)
                        edits_f_f = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', edits_f)
                        cliente = alunos[cpf_f]
                        del alunos[cpf_f]
                        alunos[edits_f_f] = cliente
                        print(cor('✔ Alteração Feita!', 1, 32, 1, True))
                        break
                else:
                    print(cor('✘ Opção inválida!', 1, 31, 1, True))
        else:
            while True:
                resp = input(f'{cor("✘ Este CPF não está cadastrado.", 1, 31, 1, True)} '
                             f'Gostaria de cadastrar? (s/n) ➔ ').lower()
                while resp.strip() == "":
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
                    resp = input(f'{cor("✘ Este CPF não está cadastrado.", 1, 31, 1, True)} '
                                 f'Gostaria de cadastrar? (s/n) ➔ ').lower()
                if resp in {"s", "sim"}:
                    adicionar_a(alunos)
                    break
                elif resp in {"n", "não", "nao"}:
                    break
                else:
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
    sleep(0.5)


def pesquisar_a(alunos):
    if alunos == {}:
        print(cor('✘ Não tem alunos cadastrados no sistema.', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                adicionar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    else:
        while True:
            cpf = input('Digite o CPF do aluno: ')
            while not Verificadores.verificar_cpf(cpf):
                print(cor("✘ CPF inválido!", 1, 31, 1, True))
                cpf = input('Digite o CPF do aluno: ')
            cpf = re.sub(r'\D', '', cpf)
            cpf_f = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
            if cpf_f in alunos:
                aluno = alunos[cpf_f]
                print(cor(f" Aluno: {aluno['nome']} - Telefone: {aluno['telefone']} - CPF: {cpf_f} ", 1, 30, 103, True))
                if 'livro' in aluno and 'saida' in aluno:
                    print(f"{aluno['livro']:<30} {aluno['saida']:>15}")
                while True:
                    resp = input('Deseja editar o aluno pesquisado? (s/n) ➔ ')
                    while resp.strip() == "":
                        print(cor('✘ Valor inválido!', 1, 31, 1, True))
                        resp = input('Deseja editar o aluno pesquisado? (s/n) ➔ ')
                    if resp in {"s", "sim"}:
                        editar_a(alunos)
                        break
                    elif resp in {"n", "não", "nao"}:
                        break
                    else:
                        print(cor('✘ Valor inválido!', 1, 31, 1, True))
            else:
                print(cor('✘ Aluno não cadastrado!', 1, 31, 1, True))
                while True:
                    resp = input('Deseja cadastrar? (s/n) ➔ ').lower()
                    while resp.strip() == "":
                        print(cor('✘ Valor inválido!', 1, 31, 1, True))
                        resp = input('Deseja Cadastrar? (s/n) ➔ ').lower()
                    if resp in {"s", "sim"}:
                        adicionar_a(alunos)
                        break
                    elif resp in {"n", "não", "nao"}:
                        break
                    else:
                        print(cor('✘ Valor inválido!', 1, 31, 1, True))
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


def listar_a(alunos):
    if alunos == {}:
        print(cor('✘ Não tem Alunos cadastrado no sistema!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                adicionar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    else:
        print(cor(f'{"Alunos":^30}⎢{"Telefone":^17}⎢{"CPF":^15}⎢', 1, 30, 43, True))
        for cpf, aluno in alunos.items():
            print(f"{aluno['nome']:<30}⎢{aluno['telefone']:<17}⎢{cpf:>15}⎢")
    sleep(0.5)


def menu():
    msg = "          Módulo de Registro de Alunos          "
    print(cor(len(msg) * " ", 1, 30, 103))
    print(msg)
    print(len(msg) * " ")
    print(cor(" 1 ➔ Cadastramento de Alunos", 7, 90, 103))
    print(" 2 ➔ Descadastramento de Alunos")
    print(" 3 ➔ Editar Cadastro de Alunos")
    print(" 4 ➔ Pesquisa de Alunos")
    print(" 5 ➔ Listagem de Alunos")
    print(" 6 🡠 Voltar")
    print(60 * "‗‗")
    return int(input(cor(" Digite sua opção: ")))


def start(database):
    while True:
        try:
            op = menu()
            if op == 1:
                sleep(0.5)
                adicionar_a(database["alunos"])
            elif op == 2:
                sleep(0.5)
                apagar_a(database["alunos"])
            elif op == 3:
                sleep(0.5)
                editar_a(database["alunos"])
            elif op == 4:
                sleep(0.5)
                pesquisar_a(database["alunos"])
            elif op == 5:
                sleep(0.5)
                listar_a(database["alunos"])
            elif op == 6:
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
