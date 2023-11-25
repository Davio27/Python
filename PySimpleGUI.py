# import PySimpleGUI as sg
# # from PySimpleGUI import PySimpleGUI as sg

# # Layout
# # sg.theme('Reddit')
# tela = [
#     [sg.Text('Usuário'), sg.Input(key='usuario')],
#     [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
#     [sg.Checkbox('Salvar o login')],
#     [sg.Button('Entrar')]
# ]

# # Janela
# janela = sg.Window('Tela de Login', tela)

# # Ler os eventos
# while True:
#     eventos, valores = janela.read()
#     if eventos == sg.WIN_CLOSED:
#         break
#     if eventos == 'Entrar':
#         if valores['usuario'] == 'davio' and valores['senha'] == '123456':
#             print('Parabens, deu tudo certo')

import PySimpleGUI as sg

# Layout
# sg.theme('Reddit')
tela = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', tela)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'davio' and valores['senha'] == '123456':
            print('Parabens, deu tudo certo')

# Fechar a janela
janela.close()
