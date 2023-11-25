import tkinter
# O tkinter.Tk tem um ponto, o 't' depois do '.' tem que ser maiusculo
janela = tkinter.Tk()
# dimenssão da janela
janela.geometry("900x700")

def clique():
    print("Fazer Login")

# titullo
texto = tkinter.Label(text= "Fazer Login")
texto.pack(padx=10, pady=10)

# botão
botao = tkinter.Button(janela, text = "Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()

