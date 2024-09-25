def cor(texto='', estilo=0, letra=31, fundo=0, fim=False):
    """Quando chamar a função, digite:
    1º o texto que vc quer mudar o estilo (obrigatório)
    2º o estilo da letra
    3º a cor da letra
    4ª cor do fundo da letra
    5º False, caso não queira que a cor tenha limite
    link: https://gist.github.com/natorsc/8de21b65036d5965346ad4a779e72e28"""
    if fim:
        return f'\033[{estilo};{letra};{fundo}m{texto}\033[m'
    else:
        return f'\033[{estilo};{letra};{fundo}m{texto}'
