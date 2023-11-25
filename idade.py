nome=input("Digite o nome da pessoa: ")
idade=int(input("Digite a idade da pessoa: "))
if idade>=18:
    print(f"Tudo certo, {nome} tem {idade}, entao ele é maior de idade")
else:
    print(f"Ele tem {idade}, entao ele é menor de idade, nao pode entrar")
