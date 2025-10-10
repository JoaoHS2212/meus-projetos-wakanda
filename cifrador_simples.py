alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 3

def cifrar(palavra, shift=3):
    cifrado = ''
    for char in palavra:
        if char in alphabet:
            indice = alphabet.index(char)
            novo_indice = (indice + shift) % 26
            cifrado += alphabet[novo_indice]
        else:
            cifrado += char
    return cifrado

def decifra(palavra, shift=-3):
    decifrado = ''
    for char in palavra:
        if char in alphabet:
            indice = alphabet.index(char)
            novo_indice = (indice + shift) % 26
            decifrado += alphabet[novo_indice]
        else:
            decifrado += char
    return decifrado


palavra = 'waka'
cifrado_test = cifrar(palavra)
print(f'Cifrado: {cifrado_test}') 
print(f'Decifrado: {decifra(cifrado_test)}') 