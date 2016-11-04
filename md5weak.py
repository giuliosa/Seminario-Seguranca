import hashlib

hasher = hashlib.md5()

hasher.update(b"noregianblue")
hasher.digest()
md_hasher = (str(hasher.hexdigest()))

password = input("Digite sua senha: ")

p = hashlib.md5(password.encode('utf-8')).hexdigest()


if(md_hasher == p):
    print("Acesso permitido")
else:
    print("Acesso negado")
input("[ENTER]")
