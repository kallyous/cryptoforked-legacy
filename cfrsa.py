from random import randrange


# Cáculo básico do MDC usando recursão
def mdc(a, b):
    if b: return mdc(b, a % b)
    return a


# Calcula, por força bruta, a inversa multiplicativa de dois números
''' Vale aqui ressaltar que esse procedimento é melhor feito usando o Algoritmo de Euclide Extendido.
    Por pressa, usei este método. É lento pra kct! '''
def multi_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# Calcula e retorna os coprimos do número solicitado.
''' Mais uma situação que merece optimização. É melhor pegar um número qualquer, aleatório, e testar se ele é
    co-primo de a. Não há necessidade de iterar todos os números. Só algumas escolhas aleatórias já basta pra
    esbarrar com um coprimo de a.'''
def coprimes(a):
    l = []
    for x in range(2, a):
        if mdc(a, x) == 1 and multi_inv(x,a) is not None:
            l.append(x)
    for x in l:
        if x == multi_inv(x, a):
            l.remove(x)
    return l


# O coração da bagaça.
''' Usando o par de primos (p q), calcula os valores de (d e n) e os retorna.'''
def genkeypair(p, q):
    n = p * q
    fi = (p - 1) * (q - 1)

    cps = coprimes(fi)
    i = randrange(0, len(cps))
    e = cps[i]

    d = multi_inv(e, fi)

    return d, e, n


# Criptografa um caracter
''' Precisa ser alterado para criptografar um byte.'''
def encryptpart(m, e, n):
    c = multi_inv(m**e, n)
    if c == None:
        print('Inversa multiplicativa do módulo é impossível para {}'.format(m))
        raise Exception;
    return c


# descriptografa um caracter
''' Precisa ser alterado para descriptografar um byte.'''
def decryptpart(c, d, n):
    m = multi_inv(c**d, n)
    if m == None:
        print('Inversa multiplicativa do módulo é impossível para {}'.format(c))
    return m


# Criptografa uma string
''' Precisa ser alterado para converter a string em bytearray e criptografar os bytes isoladamente,
    retornando então a bytearray. '''
def encrypt(plain_txt, e, n):
    cripto = []
    for c in plain_txt:
        cripto.append(chr(encryptpart(ord(c), e, n)))
    return ''.join(cripto)


# Descriptografa string criptografada
''' Precisa ser alterado apra descriptografar uma array de bytes e converter o resultado de volta em uma string.'''
def decrypt(encry_text, d, n):
    plain = []
    for c in encry_text:
        plain.append(chr(decryptpart(ord(c), d, n)))
    return ''.join(plain)
