import tkinter as tk
import customtkinter as ctk

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela de Login")
        self.root.geometry("900x900")

        self.create_login_widgets()
        self.create_signup_widgets()

    def create_login_widgets(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(side="left", fill="both", expand=True)

        ctk.CTkLabel(self.login_frame, text="Login", font=("Arial", 14)).pack(pady=10)

        ctk.CTkLabel(self.login_frame, text="Usuário:").pack()
        self.login_username = ctk.CTkEntry(self.login_frame)
        self.login_username.pack()

        ctk.CTkLabel(self.login_frame, text="Senha:").pack()
        self.login_password = ctk.CTkEntry(self.login_frame, show="*")
        self.login_password.pack()

        self.login_button = ctk.CTkButton(self.login_frame, text="Entrar", command=self.login)
        self.login_button.pack(pady=10)

    def create_signup_widgets(self):
        self.signup_frame = tk.Frame(self.root)
        self.signup_frame.pack(side="right", fill="both", expand=True)

        ctk.CTkLabel(self.signup_frame, text="Cadastro", font=("Arial", 14)).pack(pady=10)

        ctk.CTkLabel(self.signup_frame, text="Usuário:").pack()
        self.signup_username = ctk.CTkEntry(self.signup_frame)
        self.signup_username.pack()

        ctk.CTkLabel(self.signup_frame, text="Senha:").pack()
        self.signup_password = ctk.CTkEntry(self.signup_frame, show="*")
        self.signup_password.pack()

        self.signup_button = ctk.CTkButton(self.signup_frame, text="Cadastrar", command=self.signup)
        self.signup_button.pack(pady=10)

    def login(self):
        username = self.login_username.get()
        password = self.login_password.get()
        # Faça a verificação de login aqui (por exemplo, compare com valores armazenados em um banco de dados)
        print(f"Tentativa de login com usuário {username} e senha {password}")

    def signup(self):
        username = self.signup_username.get()
        password = self.signup_password.get()
        # Faça o processo de cadastro aqui (por exemplo, armazene os valores em um banco de dados)
        print(f"Tentativa de cadastro com usuário {username} e senha {password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()