import sys
import os


def genPubKey(p, q):
    e = (p-1)*(q-1)
    n = p*q
    return n, e


if __name__ == '__main__':
    print('Cryptofucked 0.0.1')
    esc = input('Escolha uma das opções:\n\n1. Gerar chave pública\n2. Criptografar\n3. Descriptografar\n')

    if esc == '1':
        print('Gerar chave pública - Insira dois números primos separados por um espaço.')
        str = input()
        p, q = str.split(' ')
        p = int(p)
        q = int(q)
        n, e = genPubKey(p, q)
        print('Chave privada:', p, q)
        print('Chave pública:', n, e)
    elif esc == '2':
        print('Criptografar...')
    elif esc == '3':
        print('Descriptografar...')
    else:
        print('Opção inválida.')
