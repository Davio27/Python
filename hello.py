from itertools import chain


print("Hello World")
nome = input("Digite o nome do aluno:")
diciplina = input("Nome da disciplina")
av1 = float(input("Digite a nota AV1:"))
av2 = float(input("Digite a nota AV2:"))
avd = float(input("Digite a nota AVD:"))

mf = (av1+av2+avd)/3
if mf < 6:
    print(nome, "está REPROVADO em", diciplina)
else: 
    print(nome, "esta APROVADO em", diciplina)

