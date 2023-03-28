from database import Database
from settings import *

class Chatroom:
    def __init__(self, window, user):
        self.win = window
        self.win.geometry('800x600')
        self.win.title('myDiscord')
        self.username = user

        self.database = Database()

        style = ttk.Style(self.win)
        style.configure('lefttab.TNotebook', tabposition='ws')
        style.configure("TNotebook", padding=[10,5])
        style.configure("TNotebook.Tab", font=LITTLE, padding=[6,2])

        self.get_all_users()
        self.draw()

    def get_all_users(self):
        self.database.my_cursor.execute("USE my_discord")
        self.database.my_cursor.execute("SELECT nickname FROM users")
        results = self.database.my_cursor.fetchall()
        self.list_pseudo = []

        for i in range(0, len(results)):
            self.list_pseudo.append(results[i][0])

        self.list_pseudo.remove(self.username)

    def draw(self):
        # Principal frame : 
        page_frame = ttk.Frame(self.win, width=800, height=600)
        page_frame.place(x=0, y=0)

        msg_frame=ttk.Frame(page_frame)
        msg_frame.pack(side="right")

        text_msg_frame = ttk.Label(msg_frame, text="PRIVATE CHAT", font=VERY_LITTLE)
        text_msg_frame.pack(side='top', padx=3, pady=15)

        for i in self.list_pseudo:
            members_button = ttk.Button(msg_frame, text = i, command=lambda: self.private_chat(self.username, i))
            members_button.pack(side="top", padx= 20, pady=5)

        disconnect_button = ttk.Button(msg_frame, text = "Log Off")
        disconnect_button.pack(side='bottom', padx=20, pady=40)

        self.tabs = ttk.Notebook(page_frame, style='lefttab.TNotebook', width=500, height=575)
        self.channel_1 = ttk.Frame(self.tabs)
        self.channel_2 = ttk.Frame(self.tabs)
        self.channel_3 = ttk.Frame(self.tabs)
        self.channel_4 = ttk.Frame(self.tabs)
        self.channel_5 = ttk.Frame(self.tabs)

        self.tabs.add(self.channel_1, text = "CHANNEL 1")
        self.tabs.add(self.channel_2, text = "CHANNEL 2")
        self.tabs.add(self.channel_3, text = "CHANNEL 3")
        self.tabs.add(self.channel_4, text = "CHANNEL 4")
        self.tabs.add(self.channel_5, text = "CHANNEL 5")
        self.tabs.pack(expand = 1, fill = "both")

        # Channel 1: 
        text_area_1 = scrolledtext.ScrolledText(self.channel_1, width=84, height=28, bd=0, bg="#3C3C3C")
        text_area_1.pack(padx=20, pady=15)
        text_area_1.config(state='disabled')

        self.input_area_1 = tk.Text(self.channel_1, height = 4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_1.pack(padx = 20, pady = 5, side='left')

        self.button_send_1 = ttk.Button(self.channel_1, text=" Send")
        self.button_send_1.pack(side="right")

        # Channel 2: 
        text_area_2 = scrolledtext.ScrolledText(self.channel_2, width=84, height=28, bd=0, bg="#3C3C3C")
        text_area_2.pack(padx=20, pady=15)
        text_area_2.config(state='disabled')

        self.input_area_2 = tk.Text(self.channel_2, height = 4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_2.pack(padx = 20, pady = 5, side='left')

        self.button_send_2 = ttk.Button(self.channel_2, text=" Send")
        self.button_send_2.pack(side="right")

        # Channel 3: 
        text_area_3 = scrolledtext.ScrolledText(self.channel_3, width=84, height=28, bd=0, bg="#3C3C3C")
        text_area_3.pack(padx=20, pady=15)
        text_area_3.config(state='disabled')

        self.input_area_3 = tk.Text(self.channel_3, height = 4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_3.pack(padx = 20, pady = 5, side='left')

        self.button_send_3 = ttk.Button(self.channel_3, text=" Send")
        self.button_send_3.pack(side="right")

        # Channel 4: 
        text_area_4 = scrolledtext.ScrolledText(self.channel_4, width=84, height=28, bd=0, bg="#3C3C3C")
        text_area_4.pack(padx=20, pady=15)
        text_area_4.config(state='disabled')

        self.input_area_4 = tk.Text(self.channel_4, height = 4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_4.pack(padx = 20, pady = 5, side='left')

        self.button_send_4 = ttk.Button(self.channel_4, text=" Send")
        self.button_send_4.pack(side="right")

        # Channel 5: 
        text_area_5 = scrolledtext.ScrolledText(self.channel_5, width=84, height=28, bd=0, bg="#3C3C3C")
        text_area_5.pack(padx=20, pady=15)
        text_area_5.config(state='disabled')

        self.input_area_5 = tk.Text(self.channel_5, height = 4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_5.pack(padx = 20, pady = 5, side='left')

        self.button_send_5 = ttk.Button(self.channel_5, text=" Send")
        self.button_send_5.pack(side="right")


    def private_chat(self, user, friend):
        window = tk.Toplevel()
        window.geometry("300x500")

        text_area = scrolledtext.ScrolledText(window, width=80, height=22)
        text_area.pack(padx=20, pady=15)
        text_area.config(state='disabled')

        self.input_area = tk.Text(window, height = 20, width=30)
        self.input_area.pack(padx = 5, pady = 10, side='left')

        self.button_send = ttk.Button(window, text=">")
        self.button_send.pack(side="right", padx=10)


    def clear_frame(self):
        for element in self.page_frame.winfo_children():
            element.destroy()