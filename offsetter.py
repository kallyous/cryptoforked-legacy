''' Fluxo de (de)codificação:
"A BC" -> encode -> "1 27 2 3" -> encrypt -> "34 54 65 78"
"34 54 65 78" -> decrypt -> "1 27 2 3" -> decode -> "A BC"
'''


offset = 65
space = 27

# Encoda string para ser criptografada
def encode_str(plain_str):
    encoded = ''
    for c in plain_str:
        encoded +=
    return encoded


# Decodifica string
def decode_list(encoded_list):
    plain_str = ''
    for n in encoded_list:
        plain_str += chr(decode_num(n))
    return plain_str


# Encoda caractere no acordo do projeto
def encode_char(c):
    if ord(c) == ord(' '): return space
    else: return ord(c) - offset


# Decoda o número de um caractere de volta ao normal
def decode_num(n):
    if n == space: return ord(' ')
    else: return n + offset
