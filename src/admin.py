import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
class AdminApp(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.state('zoomed')

        self.init_ui()

    def init_ui(self):
        original = Image.open("./super-x/assets/admin.png")
        resized = original.resize((int(original.width*0.9),int(original.height*0.9)))

        self.img = ImageTk.PhotoImage(resized)

        img_label = tk.Label(self.root, image=self.img)
        img_label.place(x=self.root.winfo_screenwidth() - 100 - resized.width, y=-10, relwidth=1, relheight=1)

        button_width = 14
        button_height = 2
        padx = 20

        self.home_button = tk.Button(self.root, text="Home",fg="#1F1467", font=("Arial", 17, "bold"), width=button_width, height=button_height, bd=0, padx=padx,cursor='hand2')
        self.home_button.place(x=3,y=20)

        self.availablecar_button = tk.Button(self.root, text="Available Cars",fg="#1F1467", font=("Arial", 17, "bold"), width=14, height=2, bd=0, padx=padx,cursor='hand2',command=self.show_availablecarinterface)
        self.availablecar_button.place(x=3,y=90)

        self.addcar_button = tk.Button(self.root, text="Add Car",fg="#1F1467", font=("Arial", 17, "bold"), width=14, height=2, bd=0, padx=padx,command=self.show_addcarinterface,cursor='hand2')
        self.addcar_button.place(x=3,y=160)

        self.transaction_button = tk.Button(self.root, text="Transactions",fg="#1F1467", font=("Arial", 17, "bold"), width=14, height=2, bd=0, padx=padx,command=self.show_transactions,cursor='hand2')
        self.transaction_button.place(x=3,y=230)

        self.logout_button = tk.Button(self.root, text="Log Out", fg="#1F1467", font=("Arial", 17, "bold"), width=14, height=2, bd=0, padx=padx,command=self.show_login,cursor='hand2')
        self.logout_button.place(x=3,y=300)
    
    def show_login(self):
        self.destroy()
        from login import LoginWindow
        login_frame = LoginWindow(self.master)
        login_frame.pack(expand=True, fill=tk.BOTH)

    def show_availablecarinterface(self):
        self.destroy()
        from availablecars import AvailableCarsInterface
        availablecars_frame = AvailableCarsInterface(self.master)
        availablecars_frame.pack(expand=True, fill=tk.BOTH)

    def show_addcarinterface(self):
        self.destroy()
        from addcar import AddCarInterface
        addcar_frame = AddCarInterface(self.master)
        addcar_frame.pack(expand=True, fill=tk.BOTH)

    def show_transactions(self):
        self.destroy()
        from adminbooking import AdminTransactionApp

        transactions_frame = AdminTransactionApp(self.master)
        transactions_frame.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminApp(root)
    root.mainloop()
