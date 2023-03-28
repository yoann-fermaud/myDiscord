from inscription import Inscription
from connexion import Connexion
from database import Database
from settings import *


class Homepage:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('800x600')
        self.win.title('myDiscord')

        self.database = Database()

        # Theme import : 
        self.win.tk.call('source', 'Tkinter_theme/forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')

    def draw_homepage(self):
        self.frame = ttk.Frame(self.win)
        self.frame.pack(pady=200)

        title = ttk.Label(self.frame, text ="MyDiscord", font=MEDIUM)
        title.pack()

        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=50)

        inscription = ttk.Button(button_frame, text="Sign In", command=lambda:[self.clear_frame(), Inscription(self.win)])
        inscription.pack(side='left', padx=20)

        connexion = ttk.Button(button_frame, text="Log In", command=lambda:[self.clear_frame(), Connexion(self.win)])
        connexion.pack(side='right', padx=20)

    def clear_frame(self):
        for element in self.frame.winfo_children():
            element.destroy()

    def create_database(self):
        self.database.create_my_discord()

    def run(self):
        self.draw_homepage()
        self.win.mainloop()


if __name__ == '__main__':
    homepage = Homepage()
    homepage.create_database()
    homepage.run()
