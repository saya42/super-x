import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials, firestore
from admin import AdminApp
from home import HomeApp
from document import DocumentApp

cred = credentials.Certificate("./super-x/setup/super-x.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()


class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.configure(background="white")
        self.init_ui()

    def init_ui(self):
        self.pack(expand=True, fill=tk.BOTH)

        script_directory = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_directory, "../assets/login.png")
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        label = tk.Label(self, image=img, bg='white')
        label.image = img 
        label.place(x=50, y=60)

        self.frame = tk.Frame(self, width=550, height=550, bg='white')
        self.frame.place(x=920, y=50)

        self.heading = tk.Label(self.frame, text='Login', fg="#57a1f8", bg='white', font=('Arial', 23, 'bold'))
        self.heading.place(x=250, y=180)

        self.user = tk.Entry(self.frame, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=160, y=253)
        self.user.insert(0, 'Username')
        self.user.bind("<FocusIn>", self.on_enter_username)
        self.user.bind("<FocusOut>", self.on_leave_username)
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=150, y=280)

        self.password = tk.Entry(self.frame, show='*', width=30, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.password.place(x=160, y=323)
        self.password.insert(0, 'Password')
        self.password.bind("<FocusIn>", self.on_enter_password)
        self.password.bind("<FocusOut>", self.on_leave_password)
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=150, y=350)

        self.button_label=tk.Button(self.frame, width=32, text='Log in', bg='#57a1f8', fg='white', border=0,font=('Microsoft YaHei UI Light', 12),command=self.login)
        self.button_label.place(x=150, y=370)

        self.label = tk.Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Arial', 11))
        self.label.place(x=140, y=420)

        self.sign_up = tk.Button(self.frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=self.show_signup)
        self.sign_up.place(x=302, y=417)

        self.back_button = tk.Button(self.frame, width=4, text='Back', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=self.back)
        self.back_button.place(x=350, y=417)

        self.Aboutus_button = tk.Button(self.frame, width=8, text='About Us', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=self.show_aboutus)
        self.Aboutus_button.place(x=385, y=417)

    def on_enter_username(self, e):
        if self.user.get() == 'Username':
            self.user.delete(0, 'end')

    def on_leave_username(self, e):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Username')

    def on_enter_password(self, e):
        if self.password.get() == 'Password':
            self.password.delete(0, 'end')

    def on_leave_password(self, e):
        name = self.password.get()
        if name == '':
            self.password.insert(0, 'Password')

    def show_aboutus(self):
        self.destroy()
        from about_us import Aboutus
        aboutus_app = Aboutus(self.master)  # Create an instance of DocumentApp
        aboutus_app.pack(expand=True, fill=tk.BOTH)


    def login(self):
        username = self.user.get()
        password = self.password.get()

        user_ref = db.collection('users').document(username)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            if user_data['Password'] == password:
                if 'admin' in user_data:
                    messagebox.showinfo("Login","Admin Logged in successfully!")
                    self.destroy()  # Close the login window
                    admin_app = AdminApp(self.master)  # Create an instance of DocumentApp
                    admin_app.pack(expand=True, fill=tk.BOTH)  # Pack the DocumentApp

                elif 'first_time' in user_data:
                    messagebox.showinfo("Login","User Logged in successfully!")
                    user_ref.update({'first_time': firestore.DELETE_FIELD})
                    self.destroy()  # Close the login window
                    documents_app = DocumentApp(self.master,username=username)  # Create an instance of DocumentApp
                    documents_app.pack(expand=True, fill=tk.BOTH)  # Pack the DocumentApp
                else:
                    messagebox.showinfo("Login","User Logged in successfully!")
                    self.destroy()  # Close the login window
                    home_app = HomeApp(self.master,username=username)  # Create an instance of DocumentApp
                    home_app.pack(expand=True, fill=tk.BOTH)  # Pack the HomeApp
            else:
                messagebox.showerror("Login","Enter Valid Username or Password")
        else:
            messagebox.showerror("Login","User Does not exist")


    def show_signup(self):
        from signup import SignupWindow
        # Destroy LandingPage frame
        self.destroy()
        # Create and show SignupWindow
        signup_frame = SignupWindow(self.master)
        signup_frame.pack(expand=True, fill=tk.BOTH)

    def back(self):
        self.destroy()
        self.frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login")
    root.state('zoomed')
    login_frame = LoginWindow(root)
    login_frame.pack(expand=True, fill=tk.BOTH)
    root.mainloop()