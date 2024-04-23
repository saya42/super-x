import tkinter as tk
from tkinter import ttk, messagebox
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./super-x/setup/super-x.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

class AddCarInterface(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Add new Vehicle")

        
        self.img_path = "./super-x/assets/addcar.png"
        self.img = tk.PhotoImage(file=self.img_path)
        img_label = tk.Label(self, image=self.img)
        img_label.place(x=20, y=-120)
        
        # Configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12))

        self.carname = tk.Entry(self, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.carname.place(x=135, y=165)
        self.carname.insert(0, 'Car Name')
        self.carname.bind("<FocusIn>", self.on_enter_carname)
        self.carname.bind("<FocusOut>", self.on_leave_carname)
        tk.Frame(self, width=295, height=2, bg='black').place(x=130, y=190)

        self.model = tk.Entry(self, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.model.place(x=135, y=215)
        self.model.insert(0, 'Model')
        self.model.bind("<FocusIn>", self.on_enter_model)
        self.model.bind("<FocusOut>", self.on_leave_model)
        tk.Frame(self, width=295, height=2, bg='black').place(x=130, y=240)

        self.year = tk.Entry(self, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.year.place(x=135, y=265)
        self.year.insert(0, 'Year')
        self.year.bind("<FocusIn>", self.on_enter_year)
        self.year.bind("<FocusOut>", self.on_leave_year)
        tk.Frame(self, width=295, height=2, bg='black').place(x=130, y=290)

        self.engine = tk.Entry(self, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.engine.place(x=135, y=315)
        self.engine.insert(0, 'Engine Type')
        self.engine.bind("<FocusIn>", self.on_enter_engine)
        self.engine.bind("<FocusOut>", self.on_leave_engine)
        tk.Frame(self, width=295, height=2, bg='black').place(x=130, y=340)
        
        self.transmission = tk.Entry(self, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.transmission.place(x=135, y=365)
        self.transmission.insert(0, 'Transmission Type')
        self.transmission.bind("<FocusIn>", self.on_enter_transmission)
        self.transmission.bind("<FocusOut>", self.on_leave_engine)
        tk.Frame(self, width=295, height=2, bg='black').place(x=130, y=390)

        self.carnumber = tk.Entry(self, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.carnumber.place(x=135, y=415)
        self.carnumber.insert(0, 'Car Number')
        self.carnumber.bind("<FocusIn>", self.on_enter_carnumber)
        self.carnumber.bind("<FocusOut>", self.on_leave_engine)
        tk.Frame(self, width=295, height=2, bg='black').place(x=130, y=440)

        self.rent = tk.Entry(self, width=30,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.rent.place(x=135, y=465)
        self.rent.insert(0, 'Rent Per Hour')
        self.rent.bind("<FocusIn>", self.on_enter_rent)
        self.rent.bind("<FocusOut>", self.on_leave_rent)
        tk.Frame(self, width=295, height=2, bg='black').place(x=130, y=490)

        # Submit button
        tk.Button(self, text="Submit",bg="#3E7AFF",fg="white",command=self.submit_info,border=0,font=('Montserrat',16,'bold'),cursor='hand2',activebackground='#3E7AFF').place(x=230,y=595)

        # # Back button
        tk.Button(self, text="Back",fg="#3E7AFF",bg='white',border=0,font=('Montserrat',14,'bold'),cursor='hand2', command=self.go_back).place(x=130,y=520)

    def on_enter_carname(self, e):
        if self.carname.get() == 'Car Name':
            self.carname.delete(0, 'end')

    def on_leave_carname(self, e):
        name = self.carname.get()
        if name == '':
            self.carname.insert(0, 'Car Name')

    def on_enter_model(self, e):
        if self.model.get() == 'Model':
            self.model.delete(0, 'end')

    def on_leave_model(self, e):
        name = self.model.get()
        if name == '':
            self.model.insert(0, 'Model')
    
    def on_enter_year(self, e):
        if self.year.get() == 'Year':
            self.year.delete(0, 'end')

    def on_leave_year(self, e):
        name = self.year.get()
        if name == '':
            self.year.insert(0, 'Year')
    
    def on_enter_engine(self, e):
        if self.engine.get() == 'Engine Type':
            self.engine.delete(0, 'end')

    def on_leave_engine(self, e):
        name = self.engine.get()
        if name == '':
            self.engine.insert(0, 'Engine Type')

    def on_enter_transmission(self, e):
        if self.transmission.get() == 'Transmission Type':
            self.transmission.delete(0, 'end')

    def on_leave_transmission(self, e):
        name = self.transmission.get()
        if name == '':
            self.transmission.insert(0, 'Transmission Type')

    def on_enter_carnumber(self, e):
        if self.carnumber.get() == 'Car Number':
            self.carnumber.delete(0, 'end')

    def on_leave_carnumber(self, e):
        name = self.carnumber.get()
        if name == '':
            self.carnumber.insert(0, 'Car Number')

    def on_enter_rent(self, e):
        if self.rent.get() == 'Rent Per Hour':
            self.rent.delete(0, 'end')

    def on_leave_rent(self, e):
        name = self.rent.get()
        if name == '':
            self.rent.insert(0, 'Rent Per Hour')

    def go_back(self):
        self.destroy()
        from admin import AdminApp
        
        admin_app = AdminApp(self.master)  # Create an instance of DocumentApp
        admin_app.pack(expand=True, fill=tk.BOTH)  # Pack the DocumentApp

    def submit_info(self):
        car_name = self.carname.get()
        model = self.model.get()
        year = self.year.get()
        engine = self.engine.get()
        transmission = self.transmission.get()
        car_number = self.carnumber.get()
        rent_per_hour = self.rent.get()

        car_data = {
            "Vehicle Name": car_name,
            "Model": model,
            "Year": year,
            "Engine Type": engine,
            "Transmission Type": transmission,
            "Car Number": car_number,
            "Rent per hour": rent_per_hour
        }

        # Add car data to Firestore
        doc_ref = db.collection("Vehicles").document(car_number)
        doc_ref.set(car_data)

        messagebox.showinfo("Success", "Car information added successfully.")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Admin Dashboard")
    root.geometry("400x300")
    AddCarInterface(root)
    root.mainloop()
