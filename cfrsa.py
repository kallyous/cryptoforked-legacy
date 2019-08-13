from random import randrange


# Cáculo básico do MDC
def mdc(a, b):
    if b: return mdc(b, a % b)
    return a


''' fin = ϕ(n) = ϕ(p*q) = (p-1)*(q-1)
    R1: 1 < e < fin
    R2: e co-primo n, ϕ(n)
'''
def gen_e_n_fin(p, q):
    fin = (p - 1) * (q - 1)
    n = p * q
    while True:
        e = randrange(2, fin)
        if mdc(e, fin) == 1 and mdc(e, n) == 1:
            return e, n, fin


# Calcula, por força bruta, a inversa multiplicativa modular de dois números
''' R1: d*e mod ϕ(n) = 1 '''
def modmultinv(e, fin):
    for d in range(1, fin):
        if (e * d) % fin == 1:
            return d
    return None


# O coração da bagaça.
''' Usando o par de primos (p q), calcula os valores de (d e n) e os retorna.
    Leia e por encrypt key ou Encriptar
    Leia d por decrypt key ou Descriptografar
    O valor de fin é a quantidade de có-primos de n, dada pefa funçao ϕ(n) = ϕ(p*q) = (p-1)*(q-1)
'''
def genkeypairs(p, q):
    e, n, fin = gen_e_n_fin(p, q)
    d = modmultinv(e, fin)
    return (e, n), (d, n)


# Criptografa um caracter
def encryptpart(m, e, n):
    return m**e % n


# descriptografa um caracter
def decryptpart(c, d, n):
    return c**d % n


# Criptografa uma string
def encrypt(plain_txt, e, n):
    cripto = ''
    for c in plain_txt:
        cripto += ' {}'.format(encryptpart(ord(c), e, n))
    return cripto.strip(' ')


# Criptografa uma string encodada pelo acordo
def encrypt_encoded(encoded_txt, e, n):
    decoded_nums = list(map(int, encoded_txt.split()))
    cripto = ''
    for c in decoded_nums:
        cripto += ' {}'.format(encryptpart(c, e, n))
    return cripto.strip(' ')


# Descriptografa string criptografada
def decrypt(encry_text, d, n):
    plain = ''
    encry_code_list = encry_text.split(' ')
    for code in encry_code_list:
        plain += chr(decryptpart(int(code), d, n))
    return plain


# Descriptografa string criptografada
def decrypt_encoded(encry_text, d, n):
    encry_nums = list(map(int, encry_text.split()))
    plain = ''
    for c in encry_nums:
        plain += ' {}'.format(decryptpart(c, d, n))
    return plain.strip()
