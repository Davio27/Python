import tkinter
import customtkinter
root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.geometry("1280x720")
root_tk.minsize(1280, 720)
class GUI:
    def __init__(self, root_tk):
        Frame1 = customtkinter.CTkFrame(root_tk)
        Frame1.pack
        frame2 = customtkinter.CTkFrame(Frame1, width=100, height=720)
        frame2.pack(pady=20,padx=20)
        frame3 = customtkinter.CTkFrame(root_tk, width=250, height=725)
        frame3.pack()
        frame3.place(anchor="w", relx=0.0, rely=0.5, relwidth=0.2, relheight=1)
        self.test()

    def test(self):
        self.switch = customtkinter.CTkSwitch(master=root_tk, text="Dark Mode", command=self.theme_change)
        self.switch.toggle(1)
        self.switch.place(relx=0.05, rely=0.05)
        self.label_width = customtkinter.CTkLabel(root_tk, text="glasses width:")
        self.label_width.place(relx=0.1, rely=0.67, anchor=tkinter.CENTER)
        self.label_height = customtkinter.CTkLabel(root_tk, text="glasses height:")
        self.label_height.place(relx=0.1, rely=0.77, anchor=tkinter.CENTER)
        self.button_add_Face = customtkinter.CTkButton(root_tk, width=200, height=50, border_width=0, corner_radius=8, hover=True, text="Adicionar Rostos", command=print("added"))
        self.button_add_Face.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)
    def theme_change(self):
        if self.switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")   
start = GUI(root_tk)
root_tk.mainloop()