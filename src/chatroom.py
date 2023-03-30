from database import Database
from settings import *


class Chatroom:
    def __init__(self, window, user):
        self.win = window
        self.win.geometry('800x600')
        self.win.title('myDiscord')
        self.nickname = user

        self.running = True
        self.gui_done = False

        self.database = Database()

        style = ttk.Style(self.win)
        style.configure('lefttab.TNotebook', tabposition='ws')
        style.configure("TNotebook", padding=[10, 5])
        style.configure("TNotebook.Tab", font=LITTLE, padding=[6, 2])

        self.get_all_users()
        self.take_history()
        self.client(HOST, PORT)

    def get_all_users(self):
        self.database.my_cursor.execute("USE my_discord")
        self.database.my_cursor.execute("SELECT nickname FROM users")
        results = self.database.my_cursor.fetchall()
        self.list_pseudo = []

        for i in range(0, len(results)):
            self.list_pseudo.append(results[i][0])

        self.list_pseudo.remove(self.nickname)

    def draw(self):
        # Principal frame : 
        page_frame = ttk.Frame(self.win, width=800, height=600)
        page_frame.place(x=0, y=0)

        msg_frame = ttk.Frame(page_frame)
        msg_frame.pack(side="right")

        text_msg_frame = ttk.Label(msg_frame, text="PRIVATE CHAT", font=VERY_LITTLE)
        text_msg_frame.pack(side='top', padx=3, pady=15)

        for i in self.list_pseudo:
            members_button = ttk.Button(msg_frame, text=i, command=lambda: self.private_chat(self.nickname, i))
            members_button.pack(side="top", padx=20, pady=5)

        disconnect_button = ttk.Button(msg_frame, text="Log Off")
        disconnect_button.pack(side='bottom', padx=20, pady=40)

        self.tabs = ttk.Notebook(page_frame, style='lefttab.TNotebook', width=500, height=575)
        self.channel_1 = ttk.Frame(self.tabs)
        self.channel_2 = ttk.Frame(self.tabs)
        self.channel_3 = ttk.Frame(self.tabs)
        self.channel_4 = ttk.Frame(self.tabs)
        self.channel_5 = ttk.Frame(self.tabs)

        self.tabs.add(self.channel_1, text="CHANNEL 1")
        self.tabs.add(self.channel_2, text="CHANNEL 2")
        self.tabs.add(self.channel_3, text="CHANNEL 3")
        self.tabs.add(self.channel_4, text="CHANNEL 4")
        self.tabs.add(self.channel_5, text="CHANNEL 5")
        self.tabs.pack(expand=1, fill="both")

        # Channel 1: 
        self.text_area_1 = scrolledtext.ScrolledText(self.channel_1, width=84, height=28, bd=0, bg="#3C3C3C")
        self.text_area_1.pack(padx=20, pady=15)
        self.text_area_1.config(state='disabled')

        self.input_area_1 = tk.Text(self.channel_1, height=4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_1.pack(padx=20, pady=5, side='left')

        self.button_send_1 = ttk.Button(self.channel_1, text=" Send",
                                        command=lambda: [self.save_message_data(), self.write_message()])
        self.button_send_1.pack(side="right")

        # Channel 2: 
        self.text_area_2 = scrolledtext.ScrolledText(self.channel_2, width=84, height=28, bd=0, bg="#3C3C3C")
        self.text_area_2.pack(padx=20, pady=15)
        self.text_area_2.config(state='disabled')

        self.input_area_2 = tk.Text(self.channel_2, height=4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_2.pack(padx=20, pady=5, side='left')

        self.button_send_2 = ttk.Button(self.channel_2, text=" Send",
                                        command=lambda: [self.save_message_data(), self.write_message()])
        self.button_send_2.pack(side="right")

        # Channel 3: 
        self.text_area_3 = scrolledtext.ScrolledText(self.channel_3, width=84, height=28, bd=0, bg="#3C3C3C")
        self.text_area_3.pack(padx=20, pady=15)
        self.text_area_3.config(state='disabled')

        self.input_area_3 = tk.Text(self.channel_3, height=4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_3.pack(padx=20, pady=5, side='left')

        self.button_send_3 = ttk.Button(self.channel_3, text=" Send",
                                        command=lambda: [self.save_message_data(), self.write_message()])
        self.button_send_3.pack(side="right")

        # Channel 4: 
        self.text_area_4 = scrolledtext.ScrolledText(self.channel_4, width=84, height=28, bd=0, bg="#3C3C3C")
        self.text_area_4.pack(padx=20, pady=15)
        self.text_area_4.config(state='disabled')

        self.input_area_4 = tk.Text(self.channel_4, height=4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_4.pack(padx=20, pady=5, side='left')

        self.button_send_4 = ttk.Button(self.channel_4, text=" Send",
                                        command=lambda: [self.save_message_data(), self.write_message()])
        self.button_send_4.pack(side="right")

        # Channel 5: 
        self.text_area_5 = scrolledtext.ScrolledText(self.channel_5, width=84, height=28, bd=0, bg="#3C3C3C")
        self.text_area_5.pack(padx=20, pady=15)
        self.text_area_5.config(state='disabled')

        self.input_area_5 = tk.Text(self.channel_5, height=4, width=50, bd=0, bg="#3C3C3C")
        self.input_area_5.pack(padx=20, pady=5, side='left')

        self.button_send_5 = ttk.Button(self.channel_5, text=" Send",
                                        command=lambda: [self.save_message_data(), self.write_message()])
        self.button_send_5.pack(side="right")

        # History : 
        for i in range(0, len(self.take_hours_1)):
            self.text_area_1.config(state='normal')
            self.text_area_1.insert('end',
                                    f"{self.take_hours_1[i]} | {self.take_nickname_1[i]} > {self.take_message_1[i]}")
            self.text_area_1.yview('end')
            self.text_area_1.config(state='disabled')

        for i in range(0, len(self.take_hours_2)):
            self.text_area_2.config(state='normal')
            self.text_area_2.insert('end',
                                    f"{self.take_hours_2[i]} | {self.take_nickname_2[i]} > {self.take_message_2[i]}")
            self.text_area_2.yview('end')
            self.text_area_2.config(state='disabled')

        for i in range(0, len(self.take_hours_3)):
            self.text_area_3.config(state='normal')
            self.text_area_3.insert('end',
                                    f"{self.take_hours_3[i]} | {self.take_nickname_3[i]} > {self.take_message_3[i]}")
            self.text_area_3.yview('end')
            self.text_area_3.config(state='disabled')

        for i in range(0, len(self.take_hours_4)):
            self.text_area_4.config(state='normal')
            self.text_area_4.insert('end',
                                    f"{self.take_hours_4[i]} | {self.take_nickname_4[i]} > {self.take_message_4[i]}")
            self.text_area_4.yview('end')
            self.text_area_4.config(state='disabled')

        for i in range(0, len(self.take_hours_5)):
            self.text_area_5.config(state='normal')
            self.text_area_5.insert('end',
                                    f"{self.take_hours_5[i]} | {self.take_nickname_5[i]} > {self.take_message_5[i]}")
            self.text_area_5.yview('end')
            self.text_area_5.config(state='disabled')

        self.gui_done = True

    def private_chat(self, user, friend):
        window = tk.Toplevel()
        window.geometry("300x500")

        text_area = scrolledtext.ScrolledText(window, width=80, height=22)
        text_area.pack(padx=20, pady=15)
        text_area.config(state='disabled')

        self.input_area = tk.Text(window, height=20, width=30)
        self.input_area.pack(padx=5, pady=10, side='left')

        self.button_send = ttk.Button(window, text=">")
        self.button_send.pack(side="right", padx=10)

    def clear_frame(self):
        for element in self.page_frame.winfo_children():
            element.destroy()

    def client(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        self.running = True

        gui_thread = threading.Thread(target=self.draw)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def write_message(self):
        exec(f"text_message = self.input_area_{self.tab_selected()}.get('1.0', 'end')")
        exec("new_message = self.time_message_sent() + ' | ' + self.nickname + ' > ' + text_message")
        exec(f"self.sock.send(new_message.encode('utf-8'))")
        exec(f"self.input_area_{self.tab_selected()}.delete('1.0', 'end')")

        # if self.tab_selected() == 1:
        #     new_message = f"{self.time_message_sent()} | {self.nickname} > {self.input_area_1.get('1.0', 'end')}"
        #     self.sock.send(new_message.encode('utf-8'))
        #     self.input_area_1.delete('1.0', 'end')
        # elif self.tab_selected() == 2:
        #     new_message = f"{self.time_message_sent()} | {self.nickname} > {self.input_area_2.get('1.0', 'end')}"
        #     self.sock.send(new_message.encode('utf-8'))
        #     self.input_area_2.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if self.gui_done:
                    exec(f"self.text_area_{self.tab_selected()}.config(state='normal')")
                    exec(f"self.text_area_{self.tab_selected()}.insert('end', message)")
                    exec(f"self.text_area_{self.tab_selected()}.yview('end')")
                    exec(f"self.text_area_{self.tab_selected()}.config(state='disabled')")

            except ConnectionAbortedError:
                break
            except:
                print("Error break")
                self.sock.close()
                break

    def time_message_sent(self):
        time = datetime.datetime.now()
        self.time_message = time.strftime('%H:%M')
        return self.time_message

    def tab_selected(self):
        self.channel_number = self.tabs.index(self.tabs.select()) + 1
        return int(self.channel_number)

    def save_message_data(self):
        columns_name = ('id_channel', 'nickname', 'hours', 'message')
        exec(
            f"values = (self.tab_selected(), self.nickname, self.time_message_sent(), self.input_area_{self.tab_selected()}.get('1.0', 'end'))")
        exec("message_data = self.database.insert_into_table('messages', columns_name, values)")
        return exec("message_data")

    def take_history(self):
        for i in range(1, 6):
            exec(f"self.take_hours_{i} = self.database.get_messages('hours', {i})")

        for i in range(1, 6):
            exec(f"self.take_nickname_{i} = self.database.get_messages('nickname', {i})")

        for i in range(1, 6):
            exec(f"self.take_message_{i} = self.database.get_messages('message', {i})")
