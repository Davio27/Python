# import PySimpleGUI as sg
from PySimpleGUI import PySimpleGUI as sg

tela = [
    sg.Text('Digite o nome do aluno'), sg.Input(key='')
]
# nome = input("Digite o nome do aluno:")
# disciplina = input("Nome da disciplina:")
# av1 = float(input("Digite a nota AV1:"))
# av2 = float(input("Digite a nota AV2:"))
# avd = float(input("Digite a nota AVD:"))

# mf=(av1+av2+avd)/3
# # arredonda a media final com duas casas decimais
# mf=round(mf,2)
# if mf < 6:
#     print(nome, "está REPROVADO em", disciplina, mf)
# else: 
#     if mf >=4 and mf < 6:
#         print(nome, "está em recuperação em", disciplina, mf)
#         print("Faça a prova AV3")
#     else: 
#         print(nome, "esta APROVADO em", disciplina, mf)
            
#         print("Parabéns!!!")
        
#         print("fim do programa")