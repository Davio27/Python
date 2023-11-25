import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        def login():
            print("Login de Usuário")
            
        def cadastro():
            print("Cadastro de Usuário")

        self.title("Painel Login")
        self.geometry("700x450")

    #    janela
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # Titulo principal da janela
        
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Painel de Login", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Botões laterais esquedos
        
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Início",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.inicio_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ajuda",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.ajuda_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Novo",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.novo_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Claro", "Escuro", "Sistema"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

       
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.home_frane_large_image_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text= "Usuario")
        self.home_frane_large_image_entry.grid(row=1, column=0, padx=10, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Login", command=login)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Novo? Cadastro", compound="right", command=cadastro)
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
       

        
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

       
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        
        self.select_frame_by_name("Início")

    def select_frame_by_name(self, name):
        
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Início" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Ajuda" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "Novo" else "transparent")

        
        if name == "Início":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Ajuda":
            self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
            self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Novo":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def inicio_button_event(self):
        self.select_frame_by_name("Iníco")

    def ajuda_button_event(self):
        self.select_frame_by_name("Ajuda")

    def novo_button_event(self):
        self.select_frame_by_name("Novo")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

