import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./super-x/setup/super-x.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

class AvailableCarsInterface(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Available Cars")
        
         # Create a style for the treeview
        style = ttk.Style(self)
        style.configure("Treeview.Heading", font=('Helvetica', 11, 'bold'))  # Increase font size and make bold

        # Create a style for the treeview
        style = ttk.Style(self)
        style.configure("Treeview", font=('Helvetica', 11))

        self.tree = ttk.Treeview(self, style="Treeview")
        self.tree["columns"] = ("Car Name", "Model", "Year", "Engine Type", "Transmission Type", "Car Number", "Rent per hour")
        self.tree.heading("#0", text="Sr No.")
        self.tree.heading("Car Name", text="Car Name")
        self.tree.heading("Model", text="Model")
        self.tree.heading("Year", text="Year")
        self.tree.heading("Engine Type", text="Engine Type")
        self.tree.heading("Transmission Type", text="Transmission Type")
        self.tree.heading("Car Number", text="Car Number")
        self.tree.heading("Rent per hour", text="Rent per hour")
        
        # Center align text in treeview
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER)

        # Set the width of columns
        self.tree.column("#0", width=50)  # Sr No.
        self.tree.column("Car Name", width=100)
        self.tree.column("Model", width=100)
        self.tree.column("Year", width=70)
        self.tree.column("Engine Type", width=100)
        self.tree.column("Transmission Type", width=120)
        self.tree.column("Car Number", width=100)
        self.tree.column("Rent per hour", width=100)

        self.tree.pack(fill=tk.BOTH, expand=1)

        self.back_button = tk.Button(self, width=10, text='Back', bg='#57a1f8', fg='white', border=0,font=('Microsoft YaHei UI Light', 14,'bold'),command=self.go_back,cursor='hand2')
        self.back_button.pack(anchor=tk.CENTER,side=tk.BOTTOM)


        self.load_available_cars()

    def load_available_cars(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve car information from Firestore
        cars = db.collection("Vehicles").get()

        # Populate treeview with car information
        for i, car in enumerate(cars, start=1):
            data = car.to_dict()
            self.tree.insert("", "end", text="",values=("","","","","",""),tags=("separator"))
            car_name = car.id
            self.tree.insert("", "end", text=i, values=(data["Vehicle Name"], data["Model"], data["Year"], data["Engine Type"], 
                                                                data["Transmission Type"], data["Car Number"], 
                                                                data["Rent per hour"]))

            if i%2==0:
                self.tree.item(self.tree.get_children()[-1],tags=("Even"))
            else:
                self.tree.item(self.tree.get_children()[-1],tags=("Odd"))
        
        self.tree.tag_configure("Even",background="#f0f0f0")
        self.tree.tag_configure("Odd",background="#f0f0f0")
    
    def go_back(self):
        self.destroy()
        from admin import AdminApp
        
        admin_app = AdminApp(self.master)  # Create an instance of DocumentApp
        admin_app.pack(expand=True, fill=tk.BOTH)  # Pack the DocumentApp

# Example usage
if __name__ == "__main__":
    app = AvailableCarsInterface()
    app.mainloop()
