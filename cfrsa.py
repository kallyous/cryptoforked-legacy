from random import randrange


def gen_e_d(p, q):
    """Gera (e, d) usando algoritmo básico de Euclides e calculando a inversa
        multiplicativa por força bruta.
        Calcula ϕ(p*q), escolhe 'e' e usa Euclides simples e encontra um 'd' válido.
        eR1: 1 < e < ϕ(p*q)
        eR2: e é co-primo de ϕ(p*q)
        dR1: e*d ≅ 1 mod p*q  →  e*d mod p*q = 1
    """
    fin = (p - 1) * (q - 1)
    while True:
        e = randrange(2, fin) # 1 não serve
        if mdc(e, fin) == 1 and mdc(e, p*q) == 1:
            d = modmultinv(e, fin)
            return e, d


def mdc(a, b):
    """Algoritmo básico de Euclides."""
    if b == 0: return a
    return mdc(b, a % b)


def genkeypairs(p, q):
    """Gera o par de chaves privada e pública.
        Com (p q), cancula n e chama função que calcula (e d)
        Monta e retorna os pares de números compondo as chaves
        pública e privada.
    """
    n = p*q
    e, d = gen_e_d(p, q)
    return (e, n), (d, n)


def encryptpart(m, e, n):
    """Criptografa um caracter"""
    #return exp_mod_rap(m, e, n)
    return (m**e) % n


def decryptpart(c, d, n):
    """Descriptografa um caracter"""
    #return exp_mod_rap(c, d, n)
    return (c**d) % n


def encrypt_encoded(encoded_txt, e, n):
    """Criptografa uma string encodada pelo acordo do projeto.
        0. Recebe string contendo os números dos caracteres encodados no acordo
            do projeto (números encodados separados por espaços).
        1. Quebramos a string em várias estrings menores, cada uma contendo os
            caracteres representando o número de um caracter encodado.
        2. Interpreta cada string da lista, obtendo o número inteiro que representa.
        3. Gera string contendo os números dos caracteres criptografados,
            separados por espaços, e a retorna.
    """
    decoded_nums = list(map(int, encoded_txt.split()))
    cripto = ''
    for c in decoded_nums:
        cripto += ' {}'.format(encryptpart(c, e, n))
    return cripto.strip(' ')


def decrypt_encoded(encry_text, d, n):
    """Descriptografa string criptografada e encodada pelo acordo do projeto.
        0. Recebe string contendo os números dos caracteres criptografados,
            separados por espaços.
        1. Quebramos a string em várias estrings menores, cada uma contendo os
            caracteres representando o número de um caracter criptografado.
        2. Interpreta cada string da lista, obtendo o número inteiro que representa.
        3. Gera string contendo os números dos caracteres descriptografados,
            separados por espaços, e a retorna.
    """
    encry_nums = list(map(int, encry_text.split()))
    plain = ''
    for c in encry_nums:
        plain += ' {}'.format(decryptpart(c, d, n))
    return plain.strip()


def modmultinv(e, fin):
    """Calcula, por força bruta, a inversa multiplicativa modular de dois números.
        dR1: d*e mod ϕ(n) = 1
    """
    for d in range(1, fin):
        if (e * d) % fin == 1:
            return d
    return None

