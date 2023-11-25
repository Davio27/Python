import customtkinter as ctk 
from customtkinter import *

cor1 = "#1e1f1e" # preta
cor2 = "#feffff" #branca
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinzento
cor5 = "#FFAB40" #Laranja

class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("255x350")
        self.config(bg=cor5)

        # # Variáveis
        # self.expressao = ""
        # self.resultado = ""

        # Frames
        frametela = ctk.CTkFrame(self, bg_color=cor3, width=235, height=50)
        frametela.grid(row=0, column=0, padx=10, pady=10)
        
        framecorpo = ctk.CTkFrame(self, width=235, height=268, bg_color=cor1)
        framecorpo.grid(row=1, column=0, padx=10, pady=5)
        
        # # Label
        # self.tela = ctk.CTkLabel(frame_tela, text=self.expressao, bg=cor3, fg=cor2, font=("Ivy 13 bold"), anchor=E, width=16)
        # self.tela.place(x=0, y=0)
        
        # # Funções
        # def btn_click(event):
        #     self.expressao += event
        #     self.tela.config(text=self.expressao)
        
        # # Botões
        # b_1 = ctk.CTkButton(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), 
        #                     relief=RAISED, overrelief=RIDGE, command=lambda: self.expressao.clear())
        # b_1.place(x=0, y=0)

        # b_0 = ctk.CTkButton(frame_corpo, text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), 
        #                     relief=RAISED, overrelief=RIDGE, command=lambda: btn_click("0"))
        # b_0.place(x=0, y=220)     
if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
