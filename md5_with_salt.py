import hashlib


salt = "1ha7"
hasher = hashlib.md5((salt + "noregianblue").encode('utf-8'))

hasher.digest()
md_hasher = (str(hasher.hexdigest()))

login = input("Digite seu login: ")
password = input("Digite sua senha: ")

p = hashlib.md5((login + password).encode('utf-8')).hexdigest()


if(md_hasher == p):
    print("Acesso permitido")
else:
    print("Acesso negado")
input("[ENTER]")
