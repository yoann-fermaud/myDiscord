from src.chatroom import Chatroom
from src.database import Database
from src.settings import *


class Inscription:
    def __init__(self, window):
        self.win = window
        self.win.geometry('800x600')
        self.win.title('myDiscord')

        self.database = Database()

        self.draw()
        self.bind_input()
        self.win.mainloop()

    def draw(self):
        page_frame = ttk.Frame(self.win, width=800, height=600)
        page_frame.place(x=0, y=0)

        # Title : 
        title_frame = ttk.Frame(page_frame)
        title_frame.pack(padx=240, pady=100)
        title = ttk.Label(title_frame, text="Inscription", font=MEDIUM)
        title.pack()

        # Input : 
        input_frame = ttk.Frame(self.win, width=800, height=300)
        input_frame.place(x=0, y=200)

        self.lastname = ttk.Entry(input_frame, justify='center', width=30)
        self.firstname = ttk.Entry(input_frame, justify='center', width=30)
        self.email = ttk.Entry(input_frame, justify='center', width=30)
        self.pseudo = ttk.Entry(input_frame, justify='center', width=30)
        self.password = ttk.Entry(input_frame, justify='center', width=30)
        self.confirmation_password = ttk.Entry(input_frame, justify='center', width=30)

        self.lastname.pack(padx=300, pady=5)
        self.firstname.pack(pady=5)
        self.email.pack(pady=5)
        self.pseudo.pack(pady=5)
        self.password.pack(pady=5)
        self.confirmation_password.pack(pady=5)

        # Placeholder : 
        self.lastname.insert(0, 'Last name')
        self.firstname.insert(0, 'First name')
        self.email.insert(0, 'Email address')
        self.pseudo.insert(0, 'Nickname')
        self.password.insert(0, 'Password')
        self.confirmation_password.insert(0, 'Confirm your password')

        button = ttk.Button(input_frame, text="Sign In", command=lambda: self.check_validity_information())
        button.pack(pady=25)

    def bind_input(self):
        self.lastname.bind("<FocusIn>", self.click_lastname)
        self.lastname.bind("<FocusOut>", self.leave_lastname)
        self.firstname.bind("<FocusIn>", self.click_firstname)
        self.firstname.bind("<FocusOut>", self.leave_firstname)
        self.email.bind("<FocusIn>", self.click_email)
        self.email.bind("<FocusOut>", self.leave_email)
        self.pseudo.bind("<FocusIn>", self.click_pseudo)
        self.pseudo.bind("<FocusOut>", self.leave_pseudo)
        self.password.bind("<FocusIn>", self.click_password)
        self.password.bind("<FocusOut>", self.leave_password)
        self.confirmation_password.bind("<FocusIn>", self.click_confirm_password)
        self.confirmation_password.bind("<FocusOut>", self.leave_confirm_password)

    def click_lastname(self, arg):
        if str(self.lastname.get()) == 'Last name' or str(self.lastname.get()) == '18 characters max !!':
            self.lastname.delete(0, 'end')

    def click_firstname(self, arg):
        if str(self.firstname.get()) == 'First name'or str(self.firstname.get()) == '18 characters max !!':
            self.firstname.delete(0, 'end')

    def click_email(self, arg):
        if str(self.email.get()) == 'Email address' or self.email.get() == 'Email already used !' or self.email.get() == "Invalid email !":
            self.email.delete(0, 'end')

    def click_pseudo(self, arg):
        if str(self.pseudo.get()) == 'Nickname' or str(self.pseudo.get()) == '18 characters max !!':
            self.pseudo.delete(0, 'end')

    def click_password(self, arg):
        if str(self.password.get()) == 'Password' or self.password.get() == '8 characters minimum !' or self.password.get() == 'Use uppercase also !' or self.password.get() == 'Use lowercase also !' or self.password.get() == 'Enter a digit !' or self.password.get() == 'Where is the special character !?':
            self.password.delete(0, 'end')

    def click_confirm_password(self, arg):
        if str(self.confirmation_password.get()) == 'Confirm your password' or self.confirmation_password.get() == "Passwords are different !":
            self.confirmation_password.delete(0, 'end')

    def leave_lastname(self, arg):
        if str(self.lastname.get()) == '':
            self.lastname.insert(0, 'Last name')

    def leave_firstname(self, arg):
        if str(self.firstname.get()) == '':
            self.firstname.insert(0, 'First name')

    def leave_email(self, arg):
        if str(self.email.get()) == '':
            self.email.insert(0, 'Email address')
    def leave_pseudo(self, arg):
        if str(self.pseudo.get()) == '':
            self.pseudo.insert(0, 'Nickname')

    def leave_password(self, arg):
        if str(self.password.get()) == '':
            self.password.insert(0, 'Password')

    def leave_confirm_password(self, arg):
        if str(self.confirmation_password.get()) == '':
            self.confirmation_password.insert(0, 'Confirm your password')

    def check_validity_information(self):
        # Lastname : 
        if len(str(self.lastname.get())) >= 18:
            self.lastname.delete(0, 'end')
            self.lastname.insert(0, '18 characters max !!')
            return False
        else:
            self.valid_lastname = str(self.lastname.get())

        # Firstname : 
        if len(str(self.firstname.get())) >= 18:
            self.firstname.delete(0, 'end')
            self.firstname.insert(0, '18 characters max !!')
            return False
        else:

            self.valid_firstname = str(self.firstname.get())

        # Nickname
        self.database.my_cursor.execute("USE my_discord")
        self.database.my_cursor.execute("SELECT nickname FROM users")
        results = self.database.my_cursor.fetchall()
        list_nickname = []

        for i in range(0, len(results)):
            list_nickname.append(results[i][0])

        if str(self.pseudo.get()) in list_nickname:
            self.pseudo.delete(0, 'end')
            self.pseudo.insert(0, 'Nickname already used !')
            return False

        if len(str(self.pseudo.get())) >= 18:
            self.pseudo.delete(0, 'end')
            self.pseudo.insert(0, '18 characters max !!')
            return False
        else:
            self.valid_pseudo = str(self.pseudo.get())

        # Password :
        if str(self.password.get()) != str(self.confirmation_password.get()):
            self.confirmation_password.delete(0, 'end')
            self.confirmation_password.insert(0, 'Passwords are different !')
            return False
        else:
            if self.check_validity_password(self.password.get()) and self.check_validity_email(self.email.get()):
                self.valid_password = str(self.password.get())
                self.valid_password=hashlib.sha256(self.valid_password.encode()).hexdigest()
                columns_name = ("first_name", "last_name", "nickname", "email", "password")
                valid_info = (
                    self.valid_firstname, self.valid_lastname, self.valid_pseudo, self.valid_email, self.valid_password)
                self.database.insert_into_table("users", columns_name, valid_info)
                Chatroom(self.win, self.valid_pseudo)


    def check_validity_email(self, check):
        self.database.my_cursor.execute("USE my_discord")
        self.database.my_cursor.execute("SELECT email FROM users")
        results = self.database.my_cursor.fetchall()
        list_mail = []

        for i in range(0, len(results)):
            list_mail.append(results[i][0])

        if str(self.email.get()) in list_mail:
            self.email.delete(0, 'end')
            self.email.insert(0, 'Email already used !')
            return False
        elif '@' not in check:
            self.email.delete(0, 'end')
            self.email.insert(0, 'Invalid email !')
            return False
        else:
            self.valid_email = check.lower()
            return self.valid_email


    def check_validity_password(self, check):
        special_char = ['$', '@', '#', '%', '*', '&', '~', '§', '!', '?', '/', '>', '<', ',', ';', '.', ':', 'µ', '£']

        if len(check) < 8:
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, '8 characters minimum !')
            return False

        elif not re.search("[A-Z]", check):
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, 'Use uppercase also !')
            return False

        elif not re.search("[a-z]", check):
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, 'Use lowercase also !')
            return False

        elif not re.search("[0-9]", check):
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, 'Enter a digit !')
            return False

        elif not any(char in special_char for char in check):
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, 'Where is the special character !?')
            return False

        return True
