import tkinter as tk
from PIL import Image, ImageTk
from login import LoginWindow
from signup import SignupWindow

class LandingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master,background="White")
        self.master = master
        self.master.title("RentWheels")
        self.init_ui()

    def init_ui(self):
        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        
        image_path = "./super-x/assets/landing.png"
        image = Image.open(image_path)
        # Resize the image to fit the screen
        image = image.resize((screen_width, screen_height))
        self.photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(self.master, image=self.photo, bg="white")
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window

        self.signup_button = tk.Button(self.master, text="Signup", bg="#DCE8FE", fg="#1F1467", font=("Arial", 14, "bold"), width=10, height=2, bd=0,activebackground="#DCE8FE",command=self.show_signup)
        self.signup_button.place(x=200,y=580)

        self.login_button = tk.Button(self.master, text="Login", bg="#DCE8FE", fg="#1F1467", font=("Arial", 14, "bold"), width=10, height=2, bd=0,activebackground="#DCE8FE",command=self.show_login)
        self.login_button.place(x=80,y=580)

    def show_signup(self):
        # Destroy LandingPage frame
        self.destroy()
        # Create and show SignupWindow
        signup_frame = SignupWindow(self.master)
        signup_frame.pack(expand=True, fill=tk.BOTH)

    def show_login(self):
        # Destroy LandingPage frame
        self.destroy()
        # Create and show Login Window
        login_frame = LoginWindow(self.master)
        login_frame.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    landing_page = LandingPage(root)
    landing_page.pack(fill="both", expand=True)
    root.mainloop()