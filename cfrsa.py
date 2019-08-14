from random import randrange


# Exponenciação rápida
''' Se 'e' for par:    b² ** (e/2)
    Se 'e' for impar:  b  * (b² ** (e-1)/2) '''
def fpow(b, e):
    # Fim de recursão
    if e < 3 and e > -3 : return b**e
    if e % 2 == 0:
        # Retorne (b*b) ** (e/2)
        return fpow(b*b, e//2)
    else:
        # Retorne b * ( (b*b) ** ((e-1)/2) )
        return b * fpow(b*b, (e-1)//2)


# Algoritmo de Euclides Estendido
''' d = mdc(a, b) = a*x + b*y
    d_ = b*x_ + (a % b)*y_
    Implementação baseada no livro "Algoritmos - Teoria e Prática", página 680
'''
def ext_eucl_mdc(a, b):
    if b == 0: return a, 1, 0
    else:
        d_, x_, y_ = ext_eucl_mdc(b, a % b)
        d = d_
        x = y_
        y = x_ - (a/b)*y_
        return d, x, y


# Exponenciação Modular Rápida
''' (a**b) % c = r
    Implementação baseada na versão do algorítmo apresentada no
    livro "Algoritmos - Teoria e Prática", página 695 
'''
def exp_mod_rap(base, power, modulus):
    c = 0
    result = 1
    power_bit_len = power.bit_length()
    for i in range(0, power_bit_len):
        c = 2*c
        result = (result*result) % modulus
        mask = 1 << i
        bit_val = power & mask
        if bit_val:
            c = c + 1
            result = (result * base) % modulus
    return result


# Gera (e d) usando o Algoritmo de Euclides Estendido
def gen_e_d(p, q):
    fin = (p - 1) * (q - 1)
    while True:
        e = randrange(2, fin)
        m, x, y = ext_eucl_mdc(e, fin)
        if m == 1:
            return e, e * x

# Gera o par de chaves privada e pública
''' Usando o par de primos (p q), calcula os valores de (d e n) e os retorna.
    Leia e por encrypt key ou Encriptar
    Leia d por decrypt key ou Descriptografar
    O valor de fin é a quantidade de có-primos de n, dada pefa funçao ϕ(n) = ϕ(p*q) = (p-1)*(q-1) '''
def genkeypairs(p, q):
    n = p*q
    e, d = gen_e_d(p, q)
    return (e, n), (d, n)


# Criptografa um caracter
def encryptpart(m, e, n):
    return exp_mod_rap(m, e, n)


# descriptografa um caracter
def decryptpart(c, d, n):
    return exp_mod_rap(c, d, n)


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


# Calcula, por força bruta, a inversa multiplicativa modular de dois números
''' R1: d*e mod ϕ(n) = 1 '''
def modmultinv(e, fin):
    for d in range(1, fin):
        if (e * d) % fin == 1:
            return d
    return None