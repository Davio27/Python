import customtkinter
from tkinter import *
from customtkinter import *

class Cardapio(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Cardápio Digital")
        self.master.geometry("800x600")

        # Lista de pratos
        self.pratos = [
            {"nome": "Lasanha", "descricao": "Massa com molho de tomate, carne moída e queijo", "preco": "R$ 25,00"},
            {"nome": "Frango à parmegiana", "descricao": "Filé de frango empanado com molho de tomate e queijo", "preco": "R$ 20,00"},
            {"nome": "Arroz com feijão", "descricao": "Arroz branco com feijão temperado", "preco": "R$ 10,00"},
            {"nome": "Pizza", "descricao": "Mussarela, tomate e orégano", "preco": "R$ 30,00"},
            {"nome": "Sorvete", "descricao": "Sorvete de creme com calda de chocolate", "preco": "R$ 8,00"}
        ]

        self.init_components()

    def init_components(self):
        # Rótulo do cardápio
        cardapio_label = customtkinter.CTkLabel(self, text="Cardápio", font=("Arial", 18, "bold"))
        cardapio_label.pack(side=TOP, padx=10 ,pady=10)


        # Frame para a lista de pratos
        pratos_frame = customtkinter.CTkFrame(self)
        pratos_frame.pack(side=LEFT, padx=10 ,pady=20)

        # Lista de pratos
        for prato in self.pratos:
            nome = prato["nome"]
            descricao = prato["descricao"]
            preco = prato["preco"]

            # Rótulo do prato
            prato_label = customtkinter.CTkLabel(pratos_frame, text=nome, font=("Arial", 14, "bold"))
            prato_label.pack(side=TOP, padx=10 ,pady=10)

            # Descrição do prato
            descricao_label = customtkinter.CTkLabel(pratos_frame, text=descricao, font=("Arial", 12))
            descricao_label.pack(side=TOP)

            # Preço do prato
            preco_label = customtkinter.CTkLabel(pratos_frame, text=preco, font=("Arial", 12, "italic"))
            preco_label.pack(side=TOP)

            # Linha separadora
            # separador = Separator(pratos_frame, orient=HORIZONTAL)
            # separador.pack(side=TOP, fill=X, padx=10, pady=10)

        # Botão de saída
        sair_button = customtkinter.CTkButton(self, text="Sair", font=("Arial", 12), command=self.master.quit)
        sair_button.pack(side=BOTTOM, padx=10, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = Cardapio(master=root)
    app.mainloop()
