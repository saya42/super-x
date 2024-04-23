import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import firebase_admin
from firebase_admin import credentials, firestore, auth, initialize_app
import random

#Initialize Firestore

cred = credentials.Certificate("./super-x/setup/super-x.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

class SignupWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("SignUp")
        self.configure(background="White")
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

        self.frame = tk.Frame(self.master, width=550, height=550, bg='white')
        self.frame.place(x=920, y=50)

        self.heading = tk.Label(self.frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Arial', 23, 'bold'))
        self.heading.place(x=250, y=55)

        self.user = tk.Entry(self.frame, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=160, y=140)
        self.user.insert(0, 'Name')
        self.user.bind("<FocusIn>", self.on_enter_name)
        self.user.bind("<FocusOut>", self.on_leave_name)
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=155, y=165)

        self.email = tk.Entry(self.frame, width=30, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.email.place(x=160, y=195)
        self.email.insert(0, 'Email')
        self.email.bind("<FocusIn>", self.on_enter_email)
        self.email.bind("<FocusOut>", self.on_leave_email)
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=155, y=220)

        self.username = tk.Entry(self.frame, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.username.place(x=160, y=250)
        self.username.insert(0, 'Username')
        self.username.bind("<FocusIn>", self.on_enter_username)
        self.username.bind("<FocusOut>", self.on_leave_username)
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=155, y=275)

        self.password = tk.Entry(self.frame, show='*', width=30, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.password.place(x=160, y=305)
        self.password.insert(0, 'Password')
        self.password.bind("<FocusIn>", self.on_enter_password)
        self.password.bind("<FocusOut>", self.on_leave_password)
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=155, y=330)

        self.mobno = tk.Entry(self.frame, width=30, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.mobno.place(x=160, y=360)
        self.mobno.insert(0, 'Mobile No')
        self.mobno.bind("<FocusIn>", self.on_enter_mobno)
        self.mobno.bind("<FocusOut>", self.on_leave_mobno)
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=155, y=385)

        self.OTP_button = tk.Button(self.frame, width=8,bg='#fff',fg='#57a1f8',border=0, text='Send OTP', cursor='hand2',command=self.generate_otp,font=('Arial', 13,'bold'))
        self.OTP_button.place(x=250, y=410)

        self.style = ttk.Style()
        self.style.configure('Square.TButton', bg='#57a1f8', fg='white', borderwidth=0)

        self.button_label=tk.Button(self.frame, width=29, text='Sign Up', bg='#57a1f8', fg='white', border=0,font=('Microsoft YaHei UI Light', 12,'bold'),command=self.sign_up)
        self.button_label.place(x=155, y=460)

        self.label = tk.Label(self.frame, text='I have an account', fg='black', bg='white', font=('Arial', 12))
        self.label.place(x=155, y=510)

        # self.style.configure('Square.TButton', bg='white', fg='#57a1f8', borderwidth=0)

        self.log_in = tk.Button(self.frame, width=8,bg='white',fg='#57a1f8',border=0, text='Log in', cursor='hand2',command=self.show_login,font=('Arial', 12,'bold'))
        self.log_in.pack()
        self.log_in.place(x=280, y=508)

        self.back_button = tk.Button(self.frame, width=8,bg='#fff',fg='#57a1f8',border=0, text='Back', cursor='hand2',command=self.back,font=('Arial', 12,'bold'))
        self.back_button.place(x=350, y=508)

        self.otp_var = tk.StringVar()

    def show_OTP(self):
        self.OTP_button.place_forget()
        self.OTP = tk.Entry(self.frame, width=30, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.OTP.place(x=160, y=415)
        self.OTP.insert(0, 'Enter OTP')
        self.OTP.bind("<FocusIn>", self.on_enter_OTP)
        self.OTP.bind("<FocusOut>", self.on_leave_OTP)
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=155, y=440)

    def generate_otp(self):
        # Generate a random 6-digit OTP
        self.generated_otp = ''.join(random.choices('0123456789', k=6))

        self.otp_var.set(self.generated_otp)
        messagebox.showinfo("OTP","Your OTP is : "+self.otp_var.get())

        self.show_OTP()

    def on_enter_name(self, e):
        if self.user.get() == 'Name':
            self.user.delete(0, 'end')

    def on_leave_name(self, e):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Name')
    
    def on_enter_email(self, e):
        if self.email.get() == 'Email':
            self.email.delete(0, 'end')

    def on_leave_email(self, e):
        name = self.email.get()
        if name == '':
            self.email.insert(0, 'Email')
    
    def on_enter_OTP(self, e):
        if self.OTP.get() == 'Enter OTP':
            self.OTP.delete(0, 'end')

    def on_leave_OTP(self, e):
        name = self.OTP.get()
        if name == '':
            self.OTP.insert(0, 'Enter OTP')

    def on_enter_username(self, e):
        if self.username.get() == 'Username':
            self.username.delete(0, 'end')

    def on_leave_username(self, e):
        name = self.username.get()
        if name == '':
            self.username.insert(0, 'Username')

    def on_enter_password(self, e):
        if self.password.get() == 'Password':
            self.password.delete(0, 'end')

    def on_leave_password(self, e):
        name = self.password.get()
        if name == '':
            self.password.insert(0, 'Password')

    def on_enter_mobno(self, e):
        if self.mobno.get() == 'Mobile No':
            self.mobno.delete(0, 'end')

    def on_leave_mobno(self, e):
        name = self.mobno.get()
        if name == '':
            self.mobno.insert(0, 'Mobile No')

    def sign_up(self):
        name = self.user.get()
        email = self.email.get()
        username = self.username.get()
        password = self.password.get()
        mobile = self.mobno.get()
        OTP = self.OTP.get() if hasattr(self, 'OTP') else None  # Check if self.OTP exists

        if name == 'Name':
            messagebox.showerror("Error", "Please enter the Name !!")
            return

        if email == 'Email':
            messagebox.showerror("Error", "Please enter the Email !!")
            return

        if username == 'Username':
            messagebox.showerror("Error", "Please enter the Username !!")
            return

        if mobile == 'Mobile No':
            messagebox.showerror("Error", "Please enter the Mobile No !!")
            return

        # Check if OTP field exists and validate OTP
        if hasattr(self, 'OTP'):
            if OTP != self.otp_var.get():
                messagebox.showerror("Error", "Please enter the Valid OTP !!")
                return
        else:
            messagebox.showerror("Error", "Please generate OTP first !!")
            return

        # Check if username already exists
        user_ref = db.collection('users').document(username)
        user_doc = user_ref.get()
        if user_doc.exists:
            messagebox.showerror("Error", "Username is already taken")
            return

        # Validate password length
        if len(password) < 6:
            messagebox.showerror("Error", "Password should be at least 6 characters long")
            return

        # Validate phone number length
        if len(mobile) != 10 or not mobile.isdigit():
            messagebox.showerror("Error", "Enter the valid phone number")
            return

        doc_ref = db.collection('users').document(username)  # Use db here instead of self.db
        doc_ref.set({
            'Name': name,
            'Email': email,
            'Phone': mobile,
            'Password': password,
            'first_time': True  # Add 'first_time' attribute
        })

        messagebox.showinfo("Signup", "User signed up successfully!")


    def show_login(self):
        from login import LoginWindow
        # Destroy LandingPage frame
        self.destroy()
        self.frame.destroy()
        # Create and show SignupWindow
        login_frame = LoginWindow(self.master)
        login_frame.pack(expand=True, fill=tk.BOTH)

    def back(self):
        self.destroy()
        self.frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Signup")
    root.state('zoomed')
    signup_frame = SignupWindow(root)
    signup_frame.pack(expand=True, fill=tk.BOTH)
    root.mainloop()