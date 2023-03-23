from Settings import *
from inscription import Inscription
from Connexion import Connexion
from database import Database

class Homepage():
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('800x600')
        self.win.title('myDiscord')
        
        # self.database = Database()

        # Theme import : 
        self.win.tk.call('source', 'Tkinter_theme/forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')

        self.draw_homepage()
        self.win.mainloop()

    def draw_homepage(self):
        background = tk.PhotoImage( file='pictures/Background.png', master=self.win)
        background_label = ttk.Label(self.win, image=background)
        background_label.place(x=0, y=0)
        # background_canvas = tk.Canvas(self.win, width=800, height=600)
        # background_canvas.pack(fill='both', expand=True)
        # background_canvas.create_image(0, 0, image=background, anchor='nw')

        title_frame = ttk.Frame(self.win)
        title_frame.pack(pady=200)

        title = ttk.Label(title_frame, text = "MyDiscord", font=MEDIUM)
        title.pack(pady=20)

        button_frame = ttk.Frame(title_frame)
        button_frame.pack(padx=100, pady=30)
        inscription = ttk.Button(button_frame, text="Inscription", command=lambda : Inscription(self.win))
        inscription.pack(side='left')
        connexion = ttk.Button(button_frame, text="Connexion", command=lambda : Connexion(self.win))
        connexion.pack(side='right', padx=40)

    # def create_database(self):
    #     self.database.create_my_discord()


if __name__ == '__main__':
    homepage = Homepage()
    # homepage.create_database()
    