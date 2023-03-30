from src.database import Database
from src.chatroom import Chatroom
from src.settings import *


class Connexion:
    def __init__(self, window) -> None:
        self.win = window
        self.win.geometry('800x600')
        self.win.title('myDiscord')

        self.database = Database()

        self.draw()
        self.bind_input()
        # self.hide_password()        

    def draw(self):
        # Principal frame :
        self.page_frame = ttk.Frame(self.win, width=800, height=500)
        self.page_frame.place(y=100)

        # Title :
        title_frame = ttk.Frame(self.page_frame)
        title_frame.pack(padx=280, pady=50)
        title = ttk.Label(title_frame, text="Connexion", font=MEDIUM)
        title.pack()

        # Input :
        input_frame = ttk.Frame(self.page_frame)
        input_frame.pack()

        self.pseudo_input = ttk.Entry(input_frame, justify='center')
        self.mdp_input = ttk.Entry(input_frame, justify='center')

        self.pseudo_input.pack(padx=300, pady=10)
        self.mdp_input.pack()

        # Placeholder :
        self.pseudo_input.insert(0, 'Pseudo')
        self.mdp_input.insert(0, 'Password')

        # Button :
        button_frame = ttk.Frame(self.page_frame)
        button_frame.pack()
        
        button = ttk.Button(button_frame, text="Connexion",
                            command=lambda: self.check_validity(self.pseudo_input.get(), self.mdp_input.get()))

        button.pack(pady=20)

    def clear_frame(self):
        for element in self.page_frame.winfo_children():
            element.destroy()
    def bind_input(self):
        self.pseudo_input.bind("<FocusIn>", self.click_pseudo)
        self.pseudo_input.bind("<FocusOut>", self.leave_pseudo)
        self.mdp_input.bind("<FocusIn>", self.click_password)
        self.mdp_input.bind("<FocusOut>", self.leave_password)

    def click_pseudo(self, arg):
        if self.pseudo_input.get() == 'Pseudo':
            self.pseudo_input.delete(0, 'end')

    def click_password(self, arg):
        if self.mdp_input.get() == 'Password' or self.mdp_input.get() == 'Incorrect password':
            self.mdp_input.delete(0, 'end')

    def leave_pseudo(self, arg):
        if self.pseudo_input.get() == '':
            self.pseudo_input.insert(0, 'Pseudo')

    def leave_password(self, arg):
        if self.mdp_input.get() == '':
            self.mdp_input.insert(0, 'Password')

    # def hide_password(self):
    #     print(str(self.mdp_input.get()))
    #     if str(self.mdp_input.get()) != "Password":
    #         self.mdp_input.config(show= "*")
    #         print(str(self.mdp_input.get()))

    def check_validity(self, pseudo, password):
        self.database.my_cursor.execute("USE my_discord")
        self.database.my_cursor.execute("SELECT nickname FROM users")
        results = self.database.my_cursor.fetchall()
        list_pseudo = []

        for i in range(0, len(results)):
            list_pseudo.append(results[i][0])

        password = hashlib.sha256(password.encode()).hexdigest()

        if pseudo in list_pseudo:
            self.database.my_cursor.execute(f"SELECT password FROM users WHERE nickname='{pseudo}'")
            saved_password = self.database.my_cursor.fetchall()
            saved_password = saved_password[0][0]

            if password == saved_password:
                self.clear_frame()
                Chatroom(self.win, pseudo)
            else:
                self.mdp_input.delete(0, 'end')
                self.mdp_input.insert(0, 'Incorrect password')
