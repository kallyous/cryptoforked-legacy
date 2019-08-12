from random import randrange


# Cáculo básico do MDC
def mdc(a, b):
    if b: return mdc(b, a % b)
    return a


# Calcula, por força bruta, a inversa multiplicativa modular de dois números
''' R1: d*e mod ϕ(n) = 1 '''
def modmultinv(e, fin):
    for d in range(1, fin):
        if (e * d) % fin == 1:
            return d
    return None


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
    cripto = []
    for c in plain_txt:
        cripto.append(chr(encryptpart(ord(c), e, n)))
    return ''.join(cripto)


# Descriptografa string criptografada
def decrypt(encry_text, d, n):
    plain = []
    for c in encry_text:
        plain.append(chr(decryptpart(ord(c), d, n)))
    return ''.join(plain)
