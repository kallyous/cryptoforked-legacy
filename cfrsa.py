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


#################################### Não Usados ##########################################


def ext_eucl_mdc(a, b):
    """ Algoritmo de Euclides Extendido (Não usado).
        mdc(a, b) = a*x + b*y
        b*x_ + (a % b)*y_
        "Algoritmos - Teoria e Prática", página 680
    """
    if b == 0: return a, 1, 0
    else:
        m_, x_, y_ = ext_eucl_mdc(b, a % b)
        m = m_
        x = y_
        y = x_ - (a/b)*y_
        return m, x, y


def exp_mod_rap(base, power, modulus):
    """Exponenciação Modular Rápida (não usado).
        "Algoritmos - Teoria e Prática", página 695.
        power_bit_len recebe a quantidade de bits armazenando o número power.
        Python usa a quantidade de bytes necessária para armazenar um número.
        Isso pode ser observado definindo números de diferentes tamanhos para
        uma variável a, e então chamando a.bit_length(). Quanto maior o número
        definindo para a, mais bits estarão em uso.
    """
    result = 1
    power_bit_len = power.bit_length()
    for i in range(0, power_bit_len):
        result = (result*result) % modulus
        mask = 1 << i
        bit_val = power & mask
        if bit_val: # bit_val != 0 ?
            result = (result * base) % modulus
    return result


def fpow(b, e):
    """Exponenciação rápida (Não usado).
        Se 'e' for par:    b² ** (e/2)
        Se 'e' for impar:  b  * (b² ** (e-1)/2)
    """
    # Fim de recursão
    if e < 3 and e > -3 : return b**e
    if e % 2 == 0:
        # Retorne (b*b) ** (e/2)
        return fpow(b*b, e//2)
    else:
        # Retorne b * ( (b*b) ** ((e-1)/2) )
        return b * fpow(b*b, (e-1)//2)


def encrypt(plain_txt, e, n):
    """Criptografa uma string (Não usado)."""
    cripto = ''
    for c in plain_txt:
        cripto += ' {}'.format(encryptpart(ord(c), e, n))
    return cripto.strip(' ')


def decrypt(encry_text, d, n):
    """Descriptografa string criptografada (Não usado)."""
    plain = ''
    encry_code_list = encry_text.split(' ')
    for code in encry_code_list:
        plain += chr(decryptpart(int(code), d, n))
    return plain
