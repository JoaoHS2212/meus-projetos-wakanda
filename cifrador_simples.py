alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
palavra = 'waka'  # Teste: vira 'ndnd'

cifrado = ''
for char in palavra:
    if char in alphabet:
        indice = alphabet.index(char)
        novo_indice = (indice + shift) % 26
        cifrado += alphabet[novo_indice]
    else:
        cifrado += char
print(f'Cifrado: {cifrado}')