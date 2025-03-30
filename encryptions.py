def inc_ascii(letter):
    letter = ord(letter)
    letter += 1
    letter = chr(letter)
    return letter

def encrypt (phrase):
    encrypted_phrase = ""
    for words in phrase.split():
        encrypted_word = ""
        for letter in words:
            encrypted_word += inc_ascii(letter)
        encrypted_phrase += encrypted_word + " "
    return encrypted_phrase.strip()

def encrypt_lambda(phrase):
    encrypted_phrase = ""
    for words in phrase.split():
        encrypted_word =  "".join(map(lambda letter: chr(ord(letter)+1),words))
        encrypted_phrase += encrypted_word + " "
    return encrypted_phrase.strip()
