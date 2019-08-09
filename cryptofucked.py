import sys
import os


def genPubKey(p, q):
    e = (p-1)*(q-1)
    n = p*q
    return e, n


# C = f(M) = M^e mod n
def encodeChar(char, e, n):
    return (ord(char) ** e) % n


def encrypt(msg, e, n):
    size = len(msg)
    ncrptd = []
    i = 0
    while(i < size):
        ncrptd.append(encodeChar(msg[i], e, n))
        i = i + 1
    return ncrptd


if __name__ == '__main__':
    print('Cryptofucked 0.0.1')
    esc = input('Escolha uma das opções:\n\n1. Gerar chave pública\n2. Criptografar\n3. Descriptografar\n')

    if esc == '1':
        print('Gerar chave pública - Insira dois números primos separados por um espaço.')
        str = input()
        p, q = str.split(' ')
        p = int(p)
        q = int(q)
        e, n = genPubKey(p, q)
        print('Chave privada:', p, q)
        print('Chave pública:', e, n)
    elif esc == '2':
        print('Criptografar...')
        str = input('Entre os dois números da chave pública, e, n: ')
        e, n = str.split(' ')
        e = int(e)
        n = int(n)
        mensagem = input('Digite a mensagem a ser criptografada:\n')
        mens_enc = encrypt(mensagem, e, n)
        print('Resultado:\n', mens_enc)
    elif esc == '3':
        print('Descriptografar...')
    else:
        print('Opção inválida.')
