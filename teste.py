from string import ascii_lowercase


def encripta(texto, n=13):
    ''' encripta o texto'''

    encriptado = ''
    for letra in texto:
        l = letra.lower()
        if l == ' ':
            encriptado += l
        elif l not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(l) + n
            l = ascii_lowercase[pos % 26]
            encriptado += l
    return encriptado

def decripta(texto, n=13):
    decriptado = ''
    for letra in texto:
        l = letra.lower()
        if l == ' ':
            decriptado += l
        elif l not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(l) - n
            l = ascii_lowercase[pos % 26]
            decriptado += l
    return decriptado
