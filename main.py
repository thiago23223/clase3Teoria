from encryptions import encrypt,encrypt_lambda
phrase = input("Ingrese la frase que quiera encriptar : ")
encrypted_phrase = encrypt(phrase)
print(f'frase encriptada : {encrypted_phrase} ')
phrase = input("Ingrese la frase que quiera encriptar : ")
encrypted_phrase = encrypt_lambda(phrase)
print(f'frase encriptada : {encrypted_phrase} ')
