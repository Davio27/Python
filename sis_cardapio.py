from tkinter import *

# Cria a janela principal
root = Tk()
root.title("Modo claro/escuro")

# Define as cores do modo claro
LIGHT_BG = "#F5F5F5"
LIGHT_FG = "black"

# Define as cores do modo escuro
DARK_BG = "#2B2B2B"
DARK_FG = "white"

# Define o modo atual
mode = "light"

# Função para alternar entre os modos claro e escuro
def toggle_mode():
    global mode
    
    if mode == "light":
        # Define as cores do modo escuro
        root.config(bg=DARK_BG)
        label.config(bg=DARK_BG, fg=DARK_FG)
        button.config(text="Modo claro", bg=DARK_BG, fg=DARK_FG)
        mode = "dark"
    else:
        # Define as cores do modo claro
        root.config(bg=LIGHT_BG)
        label.config(bg=LIGHT_BG, fg=LIGHT_FG)
        button.config(text="Modo escuro", bg=LIGHT_BG, fg=LIGHT_FG)
        mode = "light"

# Cria um rótulo na janela
label = Label(root, text="Olá, mundo!", bg=LIGHT_BG, fg=LIGHT_FG)
label.pack(pady=10)

# Cria um botão na janela para alternar entre os modos claro e escuro
button = Button(root, text="Modo escuro", bg=LIGHT_BG, fg=LIGHT_FG, command=toggle_mode)
button.pack(pady=10)

# Inicia a janela principal
root.mainloop()