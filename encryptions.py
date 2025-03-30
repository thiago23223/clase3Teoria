def inc_ascii(letter):
    """ funcion q recibe un caracter y me incrementa en 1 su ascii"""
    letter = ord(letter)
    letter += 1
    letter = chr(letter)
    return letter

def encrypt (phrase):
    """ funcion q reciba una frase y devuelve esa frase encriptada"""
    encrypted_phrase = ""
    for words in phrase.split():
        encrypted_word = ""
        for letter in words:
            encrypted_word += inc_ascii(letter)
        encrypted_phrase += encrypted_word + " "
    return encrypted_phrase.strip()

def encrypt_lambda(phrase):
    """ funcion q reciba una frase y devuelve esa frase encriptada"""
    encrypted_phrase = ""
    for words in phrase.split():
        encrypted_word =  "".join(map(lambda letter: chr(ord(letter)+1),words)) #le aplica la funcion lambda a cada uno de los caracteres de la palabra
        encrypted_phrase += encrypted_word + " "
    return encrypted_phrase.strip()
