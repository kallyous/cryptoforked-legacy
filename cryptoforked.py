from cfrsa import genkeypairs, encrypt, decrypt, modmultinv

''' Recebe a opção escolhida pelo usuário e executa as operações pertinentes a esta opção.
    Nada é de fato implementado aqui dentro, tudo referente ao RSA é chamado por funções.
    Há uma pequena exceção, de uma operação de RSA redundante, pertinente à descriptografia,
    explicada em sua própria seção. A causa dessa redundância é a própria exigência do
    trabalho de Mat. Disc. '''
def selectOption(opt):

    # Opção de gerar chaves criptográficas.
    if opt == '1':
        # São os nomes auto-descritivos dos arquivos que armazenarão informações das chaves.
        de_name = 'rsa_d_n_key.priv'
        pqe_name = 'rsa_p_q_e_key.priv'
        en_name = 'rsa_e_n_key.pub'

        # Lê entrada do usuário
        priv_key = input('Entre dois números primos distintos (p q): ')
        # Quebra string em duas, contendo os valores de q p
        p, q = priv_key.split(' ')
        # Converte q p nos números inteiros que eles descrevem e então gera chaves, obtendo todos os valores
        pub, priv = genkeypairs(int(p), int(q))

        e, n = pub
        d, n = priv

        # Salva chave privada (d n)
        with open(de_name, 'w') as file:
            file.write('{} {}'.format(d, n))
        print('Chave privada (d n) salva em', de_name)

        # Salva chave privada redundante (p q e)
        with open(pqe_name, 'w') as file:
            file.write('{} {} {}'.format(p, q, e))
        print('Chave privada (p q e) salva em', pqe_name)

        # Salva chave pública (e n)
        with open(en_name, 'w') as file:
            file.write('{} {}'.format(e, n))
        print('Chave pública (e n) salva em', en_name)

    # Opção de criptografar mensagens
    elif opt == '2':
        # Nomes auto-descritivos dos arquivos a armazenar a mensagem normal e criptografada
        plain_txt_name = 'plain.txt'
        encry_txt_name = 'encry.txt'

        # Lê mensagem a criptografar do usuário e salva
        plain_text = input('Entre o texto a criptografar: ')
        with open(plain_txt_name, 'w') as file:
            file.write(plain_text)

        # Lê chave pública (e n) do usuário
        pub_key = input('Entre o par de números da chave pública (e n): ')
        # Quebra a string contendo os valores das chaves em duas strings menores contendo cada uma um valor
        e, n = pub_key.split(' ')

        # Convertendo as strings com os valores (e n) para os números inteiros que representam, criptografa o texto
        encry_text = encrypt(plain_text, int(e), int(n))

        # Salva e exibe o texto criptografado
        with open(encry_txt_name, 'w') as file:
            file.write(encry_text)
        print('Texto criptografado:\n', encry_text, sep='')

    # Descriptografa mensagem contida em arquivo
    elif opt == '3':
        # Nome auto-descritivo do arquivo onde armazenar o resultado da descriptografia da mensagem
        decry_file_name = 'decry.txt'

        # Lê o nome do arquivo contendo a mensagem criptografada
        encry_file_name = input('Entre o nome do arquivo contendo o texto criptografado:\n')
        # Lê chave privada (p q e)
        priv_key = input('Entre os números p q e: ').strip()
        # Quebra string em strings menores contendo a representação dos valores
        p, q, e = priv_key.split(' ')
        p = int(p)  # Converte a string p no inteiro que ela representa
        q = int(q)  # Converte a string q no inteiro que ela representa
        e = int(e)  # Converte a string e no inteiro que ela representa

        ''' --------------------------------------------------------------------------------------
            Completamente desnecessário, não fosse a exigência imposta nas especificações do trabalho
            de descriptografar usando (p q e). Melhor seria descartar p q, mantendo apenas d e n.
            O que é feito aqui nada mais é do que repetir o cáculo da inversa multiplicativa modular,
            que é o nosso d. Como usamos (d n) para descriptografar e (e n) para criptografar, faz
            mais sentido armazenar-mos estas chaves e não (p q e). '''
        n = p*q
        fin = (p - 1) * (q - 1)
        d = modmultinv(e, fin)
        ''' -------------------------------------------------------------------------------------- '''

        # Carrega conteúdo criptografado do arquivo
        with open(encry_file_name, 'r') as file:
            encry_txt = file.read()
        print('Texto criptografado:\n', encry_txt, sep='')

        # Descriptografa
        decry_txt = decrypt(encry_txt, d, n)

        # Salva e exibe conteúdo descriptografado
        with open(decry_file_name, 'w') as file:
            file.write(decry_txt)
        print('Texto descriptografado:\n', decry_txt, sep='')

    # Executa os procedimentos de geração de chaves, criptografia e descriptografia para testar o programa
    elif opt == '4':
        # Escolha dos números primos (p q)
        p, q = 23, 29
        # Geração de (d e n)
        pub, priv = genkeypairs(p, q)
        e, n = pub
        d, n = priv
        # Escolha da mensagem a criptografar
        plain_str = 'Bom dia!'
        print('Texto inicial:', plain_str)
        # Criptografa mensagem
        enc_str = encrypt(plain_str, e, n)
        print('Texto criptografado:', enc_str)
        print(120 * '-')
        # Descriptografa mensagem
        final_str = decrypt(enc_str, d, n)
        print('Texto descriptografado:', final_str)


# MAIN - O programa começa aqui!
if __name__ == '__main__':
    print(120*'-')
    # Mensagem de título
    print('Cryptoforked 1.0.1a')
    print(120*'-')
    # Mensagem de opções disponíveis
    print('\nEscolha uma opção:\n\n1. Gerar chave pública\n2. Criptografar\n3. Descriptografar\n4. Debugar\n')
    # Lê opção escolhida pelo usuário
    opt = input('Opção: ')
    print(120 * '-')
    # Transmite opção escolhida para a função que chama os procedimentos pertinentes
    selectOption(opt)
    print(120 * '-')
