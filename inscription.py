from chatroom import Chatroom
from settings import *

class Inscription():
    def __init__(self, window) -> None:
        self.win = window
        self.win.geometry('800x600')
        self.win.title('myDiscord')

        self.draw()
        self.bind_input()
        self.win.mainloop()
        

    def draw(self):
        page_frame = ttk.Frame(self.win, width=800, height=600)
        page_frame.place(x=0, y=0)

        # Title : 
        title_frame = ttk.Frame(page_frame)
        title_frame.pack(padx=240, pady=100)
        title = ttk.Label(title_frame, text ="Inscription", font=MEDIUM)
        title.pack()

        # Input : 
        input_frame = ttk.Frame(self.win, width=800, height=300)
        input_frame.place(x=0, y=200)

        self.lastname = ttk.Entry(input_frame, justify='center', width= 30)
        self.firstname = ttk.Entry(input_frame, justify='center', width= 30)
        self.email = ttk.Entry(input_frame, justify='center', width= 30)
        self.pseudo = ttk.Entry(input_frame, justify='center', width= 30)
        self.password = ttk.Entry(input_frame, justify='center', width= 30)
        self.confirmation_password = ttk.Entry(input_frame, justify='center', width= 30)

        self.lastname.pack(padx=300, pady= 5)
        self.firstname.pack(pady= 5)
        self.email.pack(pady= 5)
        self.pseudo.pack(pady= 5)
        self.password.pack(pady= 5)
        self.confirmation_password.pack(pady= 5)

        # Placeholder : 
        self.lastname.insert(0, 'Last name')
        self.firstname.insert(0, 'First name')
        self.email.insert(0, 'Email address')
        self.pseudo.insert(0, 'Nickname')
        self.password.insert(0, 'Password')
        self.confirmation_password.insert(0, 'Confirm your password')

        button = ttk.Button(input_frame, text="Inscription", command= lambda : self.check_validity_information())
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
        if str(self.lastname.get()) == 'Last name':
            self.lastname.delete(0, 'end')
    def click_firstname(self, arg):
        if str(self.firstname.get()) == 'First name':
            self.firstname.delete(0, 'end')
    def click_email(self, arg):
        if str(self.email.get()) == 'Email address':
            self.email.delete(0, 'end')
    def click_pseudo(self, arg):
        if str(self.pseudo.get()) == 'Nickname':
            self.pseudo.delete(0, 'end')
    def click_password(self, arg):
        if str(self.password.get()) == 'Password':
            self.password.delete(0, 'end')
    def click_confirm_password(self, arg):
        if str(self.confirmation_password.get()) == 'Confirm your password':
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
        if len(str(self.lastname.get())) >= 18:
            self.lastname.delete(0, 'end')
            self.lastname.insert(0, '18 characters max !!')
        else:
            lastname = str(self.lastname.get())

        if len(str(self.firstname.get())) >= 18:
            self.firstname.delete(0, 'end')
            self.firstname.insert(0, '18 characters max !!')
        else:
            firstname = str(self.lastname.get())

        if len(str(self.pseudo.get())) >= 18:
            self.pseudo.delete(0, 'end')
            self.pseudo.insert(0, '18 characters max !!')
        else:
            pseudo = str(self.pseudo.get())

        if str(self.password.get()) != str(self.confirmation_password.get()):
            self.confirmation_password.delete(0, 'end')
            self.confirmation_password.insert(0, 'Passwords are different !')
        else:
            if self.check_validity_password(str(self.password.get())):
                print("Account created !!")


    def check_validity_password(self, check):
        error_value = True
        special_char =['$', '@', '#', '%', '*', '&', '~', '§', '!', '?', '/', '>', '<', ',', ';', '.', ':', 'µ', '£']

        if len(check) < 8:
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, '8 characters minimum !')
            error_value = False

        elif not re.search("[A-Z]", check):
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, 'Use uppercase also !')
            error_value = False
            
        elif not re.search("[a-z]", check):
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, 'Use lowercase also !')
            error_value = False

        elif not re.search("[0-9]", check):
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, 'Enter a digit !')
            error_value = False
            
        elif not any(char in special_char for char in check):
            self.password.delete(0, 'end')
            self.confirmation_password.delete(0, 'end')
            self.password.insert(0, 'Where is the special character !?')
            error_value = False

        return error_value
