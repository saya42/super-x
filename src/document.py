import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class DocumentApp(tk.Frame):
    def __init__(self, master,username):
        super().__init__(master)
        self.master = master
        self.master.title("E-KYC")
        self.master.state('zoomed')
        self.username = username
        self.init_ui()

    def init_ui(self):
        
        self.img_path = "./super-x/assets/documentcar.png"
        self.img = Image.open(self.img_path)
        self.img = ImageTk.PhotoImage(self.img)

        self.label = tk.Label(self.master, image=self.img, border=0, bg='white')
        self.label.image = self.img  # Keep a reference to the image
        self.label.place(x=150, y=0)
        self.frame = tk.Frame(self.master, width=430, height=1000, bg='#333333')
        self.frame.place(x=0, y=0)

        # Label for KYC
        tk.Label(self.frame, text="KYC", font=('Arial', 30, 'bold'), bg='#333333',fg='#8f622c').place(x=160, y=5)

        # Aadhar Number Entry
        tk.Label(self.frame, text="Enter your Aadhar No :", font=('Arial', 14), bg='#333333',fg='#fff').place(x=10, y=70)
        self.aadhar_entry = tk.Entry(self.frame, width=18)
        self.aadhar_entry.config(font=("Arial", 14))
        self.aadhar_entry.place(x=220, y=70)

        # Upload Front Side of Aadhar
        self.front_aadhar_label = tk.Label(self.frame, text="Upload Front Side of Aadhar :", font=('Arial', 14), bg='#333333',fg='#fff')
        self.front_aadhar_label.place(x=10, y=105)

        self.front_aadhar_button = tk.Button(self.frame, text="Upload", command=self.upload_front_aadhar)
        self.front_aadhar_button.place(x=280, y=105)

        self.front_aadhar_image_label = tk.Label(self.frame, bg='#333333')
        self.front_aadhar_image_label.place(x=10, y=140)
        
        # Upload Back Side of Aadhar
        self.back_aadhar_label = tk.Label(self.frame, text="Upload Back Side of Aadhar:", font=('Arial', 14), bg='#333333',fg='#fff')
        self.back_aadhar_label.place(x=10, y=300)

        self.back_aadhar_button = tk.Button(self.frame, text="Upload",command=self.upload_back_aadhar)
        self.back_aadhar_button.place(x=280, y=300)

        self.back_aadhar_image_label = tk.Label(self.frame, bg='#333333')
        self.back_aadhar_image_label.place(x=10, y=335)

        # Do you have driving licence?
        tk.Label(self.frame, text="Do you have a driving licence?", font=('Arial', 14), bg='#333333',fg='#fff').place(x=10, y=495)
        self.driving_licence_var = tk.StringVar(value="No")
        self.yes_button = tk.Radiobutton(self.frame, text="Yes", variable=self.driving_licence_var, value="Yes", command=self.show_licence_upload)
        self.yes_button.place(x=300, y=495)
        self.no_button = tk.Radiobutton(self.frame, text="No", variable=self.driving_licence_var, value="No", command=self.show_licence_message)
        self.no_button.place(x=365, y=495)
        
        # Upload Driving Licence
        self.upload_licence_label = tk.Label(self.frame, text="Upload Driving Licence :", font=('Arial', 14),bg='#333333',fg='#fff')
        self.licence_button = tk.Button(self.frame, text="Upload", command=self.upload_licence)

        self.licence_image_label = tk.Label(self.frame, bg='#333333')
        self.licence_image_label.place(x=10, y=585)

        self.submit_button = tk.Button(self.frame, text="Submit", width=20,command=self.submit)
        self.submit_button.pack()
        self.submit_button.pack_forget()

    def upload_front_aadhar(self):
        self.front_aadhar_image_path = filedialog.askopenfilename()
        if self.front_aadhar_image_path:
            image = Image.open(self.front_aadhar_image_path)
            image = image.resize((300, 150))
            photo = ImageTk.PhotoImage(image)
            self.front_aadhar_image_label.config(image=photo)
            self.front_aadhar_image_label.image = photo  # keep a reference to the image to prevent garbage collection
            messagebox.showinfo("Success", "Aadhar card front side uploaded successfully.")

    def upload_back_aadhar(self):
        self.back_aadhar_image_path = filedialog.askopenfilename()
        if self.back_aadhar_image_path:
            image = Image.open(self.back_aadhar_image_path)
            image = image.resize((300, 150))
            photo = ImageTk.PhotoImage(image)
            self.back_aadhar_image_label.config(image=photo)
            self.back_aadhar_image_label.image = photo  # keep a reference to the image to prevent garbage collection
            messagebox.showinfo("Success", "Aadhar card back side uploaded successfully.")

    def show_licence_upload(self):
        if self.driving_licence_var.get() == "Yes":
            self.upload_licence_label.place(x=10, y=545)
            self.licence_button.place(x=280, y=545)

        else:
            self.upload_licence_label.place_forget()
            self.licence_button.place_forget()

    def show_licence_message(self):
        if self.driving_licence_var.get() == "No":
            messagebox.showerror("Error", "Driving licence is mandatory for our service.")
            self.upload_licence_label.place_forget()
            self.licence_button.place_forget()
            self.licence_image_label.place_forget()
            self.submit_button.place_forget()

    def upload_licence(self):
        self.licence_image_path = filedialog.askopenfilename()
        if self.licence_image_path:
            image = Image.open(self.licence_image_path)
            image = image.resize((300, 150))
            photo = ImageTk.PhotoImage(image)
            self.licence_image_label.config(image=photo)
            self.licence_image_label.image = photo  # keep a reference to the image to prevent garbage collection
            messagebox.showinfo("Success", "Driving licence uploaded successfully.")
            self.licence_image_label.place(x=10, y=585)
            self.submit_button.place(x=130, y=750)

    def submit(self):

        aadharNo = self.aadhar_entry.get()

        # Validate phone number length
        if len(aadharNo) != 12 or not aadharNo.isdigit():
            messagebox.showerror("Error", "Enter the valid Aadhar No !!")
            return
        
        messagebox.showinfo("Success", "Data submitted successfully.")
        self.destroy()

        from home import HomeApp
        Home_page = HomeApp(self.master,self.username)
        Home_page.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    app = DocumentApp(root)
    root.mainloop()