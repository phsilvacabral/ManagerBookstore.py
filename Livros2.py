from time import sleep
import Alunos
from datetime import date, datetime
import re
import Verificadores
import Livros
from utilidades import cor


def saida_l_e(alunos, livros_livres, livros_emprestados):
    if livros_emprestados == {} and livros_livres == {}:
        print(cor('✘ Não tem nenhum livro cadastrado no estoque!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                Livros.entrada_l_n(livros_livres, livros_emprestados)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    elif alunos == {}:
        print(cor('✘ Não tem nenhum aluno cadastrado no sistema!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                Alunos.adicionar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    elif not any(v['quantidade'] >= 1 for v in livros_livres.values()):
        print(cor('✘ Nenhum livro está disponível no momento!', 1, 31, 1, True))
    else:
        cpf = input("Digite o CPF: ")
        while not Verificadores.verificar_cpf(cpf):
            print(cor("✘ CPF inválido!", 1, 31, 1, True))
            cpf = input("Digite o CPF: ")
        cpf = re.sub(r'\D', '', cpf)
        cpf_f = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
        if cpf_f not in alunos:
            while True:
                resp = input(f'{cor("✘ Este CPF não está cadastrado.", 1, 31, 1, True)} '
                             f'Deseja cadastrar? (s/n) ➔ ').lower()
                while resp.strip() == "":
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
                    resp = input(f'{cor("✘ Este CPF não está cadastrado.", 1, 31, 1, True)} '
                                 f'Deseja cadastrar? (s/n) ➔ ').lower()
                if resp in {"s", "sim"}:
                    Alunos.adicionar_a(alunos)
                    break
                elif resp in {"n", "não", "nao"}:
                    break
                else:
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
        else:
            if 'livro' in alunos[cpf_f]:
                print(cor('✘ Já existe um livro em empréstimo neste CPF!', 1, 31, 1, True))
            else:
                livro = input('Digite o Livro: ').lower()
                while livro.strip() == "":
                    print(cor("✘ Livro inválido!", 1, 31, 1, True))
                    livro = input('Digite o Livro: ').lower()
                while livro not in livros_livres.keys():
                    print(cor(f'✘ Não temos o Livro {livro} :(', 1, 31, 1, True))
                    livro = input('Tente outro: ').lower()
                    while livro.strip() == "":
                        print(cor("✘ Livro inválido!", 1, 31, 1, True))
                        livro = input('Digite o Livro: ').lower()
                if livros_livres[livro]['quantidade'] == 0:
                    print(cor(f'✘ Não temos {livro} disponível para emprestar :(', 1, 31, 1, True))
                else:
                    while True:
                        data_str = input("Digite a data de entrada (formato: DD/MM/AAAA): ")
                        if not data_str.strip():
                            print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} Por favor, digite uma data.")
                            continue
                        if not re.match(r'^\d{2}/\d{2}/\d{4}$', data_str):
                            print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} "
                                  f"Por favor, digite uma data válida no formato DD/MM/AAAA.")
                            continue
                        try:
                            dia, mes, ano = map(int, data_str.split('/'))
                            data_saida = datetime(ano, mes, dia).date()
                            data_formatada_saida = data_saida.strftime("%d/%m/%Y")
                        except ValueError:
                            print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} "
                                  f"Por favor, digite uma data válida no formato DD/MM/AAAA.")
                            continue
                        break
                    data_str = data_str.replace("/", "")
                    data_str = data_str[:2] + "/" + data_str[2:4] + "/" + data_str[4:]
                    dia, mes, ano = map(int, data_str.split('/'))
                    data_saida = datetime(ano, mes, dia).date()
                    data_formatada_saida = data_saida.strftime("%d/%m/%Y")
                    livros_livres[livro]['quantidade'] -= 1
                    alunos[cpf_f].update({"livro": livro, 'saida': data_formatada_saida})
                    livros_emprestados[livro]['quantidade'] += 1
                    print(cor('✔ Empréstimo realizado!', 1, 32, 1, True))
    sleep(0.5)


def entrada_l_e(alunos, livros_livres, livros_emprestados):
    if livros_emprestados == {} and livros_livres == {}:
        print(cor('✘ Não tem nenhum livro cadastrado no estoque!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                Livros.entrada_l_n(livros_livres, livros_emprestados)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    elif alunos == {}:
        print(cor('✘ Não tem nenhum aluno cadastrar no sistema!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                Alunos.adicionar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    elif not any(v['quantidade'] >= 1 for v in livros_emprestados.values()):
        print(cor('✘ Nenhum livro está sendo emprestado no momento!', 1, 31, 1, True))
    else:
        cpf = input("Digite o CPF: ")
        while not Verificadores.verificar_cpf(cpf):
            print(cor("✘ CPF inválido!", 1, 31, 1, True))
            cpf = input("Digite o CPF: ")
        cpf = re.sub(r'\D', '', cpf)
        cpf_f = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
        if cpf_f not in alunos:
            while True:
                resp = input(f'{cor("✘ Este CPF não está cadastrado no sistema", 1, 31, 1, True)}. '
                             f'Deseja cadastrar? (s/n) ➔ ').lower()
                while resp.strip() == "":
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
                    resp = input(f'{cor("✘ Este CPF não está cadastrado no sistema", 1, 31, 1, True)}. '
                                 f'Deseja cadastrar? (s/n) ➔ ').lower()
                if resp in {"s", "sim"}:
                    Alunos.adicionar_a(alunos)
                    break
                elif resp in {"n", "não", "nao"}:
                    break
                else:
                    print(cor('✘ Valor inválido!', 1, 31, 1, True))
        else:
            if 'livro' not in alunos[cpf_f]:
                print(cor('✘ Não há nenhum livro registrado neste CPF!', 1, 31, 1, True))
                while True:
                    resp = input('Deseja registrar um livro? (s/n) ➔ ').lower()
                    while resp.strip() == "":
                        print(cor('✘ Valor inválido!', 1, 31, 1, True))
                        resp = input('Deseja registrar um livro? (s/n) ➔ ').lower()
                    if resp in {"s", "sim"}:
                        saida_l_e(alunos, livros_livres, livros_emprestados)
                        break
                    elif resp in {"n", "não", "nao"}:
                        break
                    else:
                        print(cor('✘ Valor inválido!', 1, 31, 1, True))
            else:
                while True:
                    data_str = input("Digite a data de entrada (formato: DD/MM/AAAA): ")
                    if not data_str.strip():
                        print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} Por favor, digite uma data.")
                        continue
                    if not re.match(r'^\d{2}/\d{2}/\d{4}$', data_str):
                        print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} "
                              f"Por favor, digite uma data válida no formato DD/MM/AAAA.")
                        continue
                    try:
                        dia, mes, ano = map(int, data_str.split('/'))
                        data_entrada = datetime(ano, mes, dia).date()
                    except ValueError:
                        print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} "
                              f"Por favor, digite uma data válida no formato DD/MM/AAAA.")
                        continue
                    break
                data_str = data_str.replace("/", "")
                data_str = data_str[:2] + "/" + data_str[2:4] + "/" + data_str[4:]
                dia, mes, ano = map(int, data_str.split('/'))
                data_entrada = date(ano, mes, dia)
                data_saida_aluno = datetime.strptime(alunos[cpf_f]['saida'], "%d/%m/%Y").date()
                dias_atraso = (data_entrada - data_saida_aluno).days
                if dias_atraso > 0 and dias_atraso > 10:
                    multa = 5 + (0.1 * (dias_atraso - 10))
                    print(cor(f'O Aluno deve pagar R${multa:.2f} de multa.', 1, 31, 1, True))
                    livro = alunos[cpf_f]['livro']
                    livros_livres[livro]['quantidade'] += 1
                    livros_emprestados[livro]['quantidade'] -= 1
                    del alunos[cpf_f]['livro']
                    del alunos[cpf_f]['saida']
                else:
                    print(cor('✔ Não tem multa!', 1, 32, 1, True))
                    livro = alunos[cpf_f]['livro']
                    livros_livres[livro]['quantidade'] += 1
                    livros_emprestados[livro]['quantidade'] -= 1
                    del alunos[cpf_f]['livro']
                    del alunos[cpf_f]['saida']
    sleep(0.5)


def devendo(alunos, livros_livres, livros_emprestados):
    if livros_emprestados == {} and livros_livres == {}:
        print(cor('✘ Não tem nenhum livro cadastrado no estoque!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                Livros.entrada_l_n(livros_livres, livros_emprestados)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    elif alunos == {}:
        print(cor('✘ Não tem nenhum aluno cadastrado no sistema!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                Alunos.adicionar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    elif not any(v['quantidade'] >= 1 for v in livros_emprestados.values()):
        print(cor('✘ Nenhum livro está sendo emprestado no momento!', 1, 31, 1, True))
    else:
        data_entrada = None
        while data_entrada is None:
            data_str = input("Digite a data de entrada (formato: DD/MM/AAAA): ")
            if not data_str.strip():
                print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} Por favor, digite uma data.")
                continue
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', data_str):
                print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} "
                      f"Por favor, digite uma data válida no formato DD/MM/AAAA.")
                continue
            dia, mes, ano = map(int, data_str.split('/'))
            try:
                data_entrada = datetime(ano, mes, dia).date()
                data_formatada_entrada = data_entrada.strftime("%d/%m/%Y")
            except ValueError:
                print(f"{cor('✘ Data inválida.', 1, 31, 1, True)} "
                      f"Por favor, digite uma data válida no formato DD/MM/AAAA.")
                data_entrada = None
                continue
            devolucao_atrasada = False
            for cpf, aluno in alunos.items():
                if "saida" in aluno:
                    data_saida_aluno = datetime.strptime(aluno['saida'], "%d/%m/%Y").date()
                    if (data_entrada - data_saida_aluno).days >= 10:
                        print(cor(f" Aluno: {aluno['nome']} - Telefone: {aluno['telefone']} - "
                                  f"CPF: {cpf} ", 1, 30, 44, True))
                        print(cor(f"Livro com devolução atrasada: {aluno['livro']} ({aluno['saida']})", 1, 31, 1, True))
                        devolucao_atrasada = True
                        sleep(0.5)
            if not devolucao_atrasada:
                print(cor("✔ Não há alunos com livros em atraso na devolução!", 1, 32, 1, True))
    sleep(0.5)


def lista(alunos, livros_livres, livros_emprestados):
    if livros_emprestados == {} and livros_livres == {}:
        print(cor('✘ Não tem nenhum livro cadastrado no estoque!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um livro? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                Livros.entrada_l_n(livros_livres, livros_emprestados)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    elif alunos == {}:
        print(cor('✘ Não tem nenhum aluno cadastrado no sistema!', 1, 31, 1, True))
        while True:
            resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            while resp.strip() == "":
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
                resp = input('Deseja cadastrar um aluno? (s/n) ➔ ').lower()
            if resp in {"s", "sim"}:
                Alunos.adicionar_a(alunos)
                break
            elif resp in {"n", "não", "nao"}:
                break
            else:
                print(cor('✘ Valor inválido!', 1, 31, 1, True))
    else:
        if not any(v['quantidade'] >= 1 for v in livros_emprestados.values()):
            print(cor('✘ Nenhum livro está sendo emprestado no momento!', 1, 31, 1, True))
        else:
            for k, v in livros_emprestados.items():
                if v['quantidade'] >= 1:
                    print(cor(f" {k:<45} ➔  Quantidade: {v['quantidade']} ", 1, 30, 44, True))
                    for aluno_cpf, aluno_info in alunos.items():
                        if 'livro' in aluno_info and k in aluno_info['livro']:
                            print(f"Aluno: {aluno_info['nome']} - ({aluno_info['livro']}) - "
                                  f"({aluno_info['saida']} - CPF: {aluno_cpf})")
    sleep(0.5)


def menu():
    msg = "          Módulo de Empréstimo          "
    print(cor(len(msg) * " ", 1, 30, 104))
    print(msg)
    print(len(msg) * " ")
    print(cor(" 1 ➔ Empréstimo de Livros", 7, 35, 90))
    print(" 2 ➔ Devolução de Livros")
    print(" 3 ➔ Verificar Devoluções em Atraso")
    print(" 4 ➔ Livros em Empréstimos")
    print(" 5 🡠 Voltar")
    print(60 * "‗‗")
    return int(input(cor(" Digite sua opção: ")))


def start(database):
    while True:
        try:
            op = menu()
            if op == 1:
                sleep(0.5)
                saida_l_e(database["alunos"], database["livros_livres"], database["livros_emprestados"])
            elif op == 2:
                sleep(0.5)
                entrada_l_e(database["alunos"], database["livros_livres"], database["livros_emprestados"])
            elif op == 3:
                sleep(0.5)
                devendo(database["alunos"], database["livros_livres"], database["livros_emprestados"])
            elif op == 4:
                sleep(0.5)
                lista(database["alunos"], database["livros_livres"], database["livros_emprestados"])
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
