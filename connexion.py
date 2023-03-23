from database import Database
from chatroom import Chatroom
from settings import *

class Connexion:
    def __init__(self, window) -> None:
        self.win = window
        self.win.geometry('800x600')
        self.win.title('myDiscord')

        # self.database = Database()
        # self.database.create_my_discord()

        self.draw()
        self.bind_input()
        # self.hide_password()        

    def draw(self):
        # Principal frame : 
        page_frame = ttk.Frame(self.win, width=800, height=600)
        page_frame.place(x=0, y=0)

        # Title : 
        title_frame = ttk.Frame(page_frame)
        title_frame.pack(padx=270, pady=130)
        title = ttk.Label(title_frame, text ="Connexion", font=MEDIUM)
        title.pack()

        # Input : 
        input_frame = ttk.Frame(self.win, width=800, height=300)
        self.pseudo_input = ttk.Entry(input_frame, justify='center')
        self.mdp_input = ttk.Entry(input_frame, justify='center')

        input_frame.place(x=0, y=230)
        self.pseudo_input.pack(padx=320, pady= 10)
        self.mdp_input.pack()

        # Placeholder : 
        self.pseudo_input.insert(0, 'Pseudo or email')
        self.mdp_input.insert(0, 'Password')

        # self.hide_password = self.mdp_input.get()
        # print(self.hide_password)
        # if self.hide_password != "Password":
        #     print("different")
        #     self.mdp_input["show"] = "*"

        # Button : 
        button = ttk.Button(input_frame, text="Connexion")
        button.pack(pady=25)

    def bind_input(self):
        self.pseudo_input.bind("<FocusIn>", self.click_pseudo)
        self.pseudo_input.bind("<FocusOut>", self.leave_pseudo)
        self.mdp_input.bind("<FocusIn>", self.click_password)
        self.mdp_input.bind("<FocusOut>", self.leave_password)
        

    def click_pseudo(self, arg):
        if str(self.pseudo_input.get()) == 'Pseudo or email':
            self.pseudo_input.delete(0, 'end')

    def click_password(self, arg):
        if str(self.mdp_input.get()) == 'Password':
            self.mdp_input.delete(0, 'end')

    def leave_pseudo(self, arg):
        if str(self.pseudo_input.get()) == '':
            self.pseudo_input.insert(0, 'Pseudo or email')

    def leave_password(self, arg):
        if str(self.mdp_input.get()) == '':
            self.mdp_input.insert(0, 'Password')

    # def hide_password(self):
    #     print(str(self.mdp_input.get()))
    #     if str(self.mdp_input.get()) != "Password":
    #         self.mdp_input.config(show= "*")
    #         print(str(self.mdp_input.get()))

# p1 = Connexion()