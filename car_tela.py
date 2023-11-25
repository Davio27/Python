

import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
from pathlib import Path
import os

# Criando a janela
window = ctk.CTk()
window._set_appearance_mode("green")

# Definindo o título da janela
window.title('Cardápio Digital')

# Definindo as dimensões da janela
window.geometry('900x700')

# importar imagem
image = Image.open('C:\\Users\\davic\\OneDrive\\Documentos\\main project\\examples\\bg_gradient.jpg')

# Converta a imagem em um objeto de imagem tkinter
photo = ImageTk.PhotoImage(image)

# Crie um widget Label com a imagem e coloque-o na janela
label = ctk.CTkLabel(window, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Criando um rót para o dopio
Titulo = ctk.CTkLabel(window, text = 'CARDÁPIO', font=ctk.CTkFont(size=40, weight="bold"))
Titulo.pack(pady=10)

butao = ctk.CTkButton(window, text= "Pesquisa",)
butao.pack(padx=10, pady=10)

# Criando um rótulo para a entrada
entry_label = ctk.CTkLabel(window, text='Entrada', font=('Arial', 25, 'underline')).place(x=20,y=60)
# entry_label.pack(pady=10)

# Criando um rótulo para a descrição da entrada
entry_description = ctk.CTkLabel(window, text='Salada de folhas comoutons', font=('Arial', 14)).place(x=20,y=100)
# entry_description.pack(pady=5)

# Criando um rótulo para o preço da entrada
entry_price = ctk.CTkLabel(window, text='R$ 12,00', font=('Arial', 14))
entry_price.pack(pady=5)

# Criando um rótulo para o prato principal
main_course_label = ctk.CTkLabel(window, text='Prato Principal', font=('Arial', 16, 'underline'))
main_course_label.pack(pady=10)

# Criando um rótulo para a descrição do prato principal
main_course_description = ctk.CTkLabel(window, text='Frango grelhado com legumes e arroz', font=('Arial', 14))
main_course_description.pack(pady=5)

# Criando um rótulo para o preço do prato principal
main_course_price = ctk.CTkLabel(window, text='R$ 20,',font=('Arial', 14))
main_course_price.pack(pady=5)

dess_label = ctk.CTkLabel(window, text='Sobremesa', font=('Arial', 16, 'underline'))
dess_label.pack(pady=10)

# Criando um rótulo para a descrição da sobremesa
dessert_description = ctk.CTkLabel(window, text='Bolo de chocolate com calda de morango', font=('Arial', 14))
dessert_description.pack(pady=5)

# Criando um rótulo para o preço da sobremesa
dessert_price = ctk.CTkLabel(window, text='R$ 8,00', font=('Arial', 14))
dessert_price.pack(pady=5)

# Iniciando a janela
window.mainloop()