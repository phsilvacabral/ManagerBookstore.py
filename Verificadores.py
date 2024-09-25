

def verificar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    digito_verificador_1 = int(cpf[9])
    digito_verificador_2 = int(cpf[10])
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != digito_verificador_1:
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != digito_verificador_2:
        return False
    return True


def verificar_n_t(numero):
    DDD = ['11', '12', '13', '14', '15', '16', '11', '17', '18', '19', '21', '22', '24', '27',
           '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46',
           '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67',
           '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86',
           '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']
    numero = numero.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    if len(numero) != 11 or not numero.isdigit():
        return False
    if numero[2] != "9":
        return False
    if numero[0:2] not in DDD:
        return False
    return True
