import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("./super-x/setup/super-x.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

class AdminTransactionApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Admin Booking")

        # Create a style for the treeview
        style = ttk.Style(self)
        style.configure("Treeview.Heading", font=('Helvetica', 11, 'bold'))  # Increase font size and make bold

        # Create a style for the treeview
        style = ttk.Style(self)
        style.configure("Treeview", font=('Helvetica', 11))

        # Create frame for treeview and button
        self.tree_frame = tk.Frame(self)
        self.tree_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, style="Treeview")
        self.tree["columns"] = ("Name", "Vehicle Name", "Pickup Date", "Pickup Time", "Drop Date", "Drop Time", "Location", "Total Payment", "Trip Protection")
        self.tree.heading("#0", text="Sr No.")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Vehicle Name", text="Vehicle Name")
        self.tree.heading("Pickup Date", text="Pickup Date")
        self.tree.heading("Pickup Time", text="Pickup Time")
        self.tree.heading("Drop Date", text="Drop Date")
        self.tree.heading("Drop Time", text="Drop Time")
        self.tree.heading("Location", text="Location")
        self.tree.heading("Total Payment", text="Total Payment")
        self.tree.heading("Trip Protection", text="Trip Protection")
        
        # Center align text in treeview
        self.tree.column("#0", anchor=tk.CENTER)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER)

        # Set the width of columns
        self.tree.column("#0", width=50)  # Sr No.
        self.tree.column("Name", width=100)
        self.tree.column("Vehicle Name", width=100)
        self.tree.column("Pickup Date", width=100)
        self.tree.column("Pickup Time", width=100)
        self.tree.column("Drop Date", width=100)
        self.tree.column("Drop Time", width=100)
        self.tree.column("Location", width=150)
        self.tree.column("Total Payment", width=100)
        self.tree.column("Trip Protection", width=100)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # # Create a vertical scrollbar
        # self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        # self.tree.configure(yscrollcommand=self.scrollbar.set)

        # self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.load_booking_info()

        self.back_button = tk.Button(self, width=10, text='Back', bg='#57a1f8', fg='white', border=0, font=('Microsoft YaHei UI Light', 14,'bold'), command=self.go_back, cursor='hand2')
        self.back_button.pack(anchor=tk.CENTER, side=tk.BOTTOM)
    

    def go_back(self):
        self.destroy()
        from admin import AdminApp
        
        admin_app = AdminApp(self.master)  # Create an instance of DocumentApp
        admin_app.pack(expand=True, fill=tk.BOTH)  # Pack the DocumentApp

    def load_booking_info(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve booking info from Firestore
        booking_info = db.collection("booking_info").get()

        # Populate treeview with booking info
        for i, booking in enumerate(booking_info):
            data = booking.to_dict()
            vehicle_name = data.get("Vehicle Name", "")
            self.tree.insert("", "end", text="", values=("","","","","","","",""), tags=("separator"))
            # Insert the data into the Treeview with correct columns
            self.tree.insert("", "end", text=str(i+1), values=(data["Name"], vehicle_name, data["Pickup Date"], data["Pickup Time"], data["Drop Date"], data["Drop Time"], data["Location"], 
                                                               data["Total Payment"], data["Trip Protection"]))

            # Apply alternating row colors
            if i % 2 == 0:
                self.tree.item(self.tree.get_children()[-1], tags=("Even"))
            else:
                self.tree.item(self.tree.get_children()[-1], tags=("Odd"))

        # Configure alternating row colors
        self.tree.tag_configure("Even", background="#f0f0f0")
        self.tree.tag_configure("Odd", background="#f0f0f0")


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminTransactionApp(root)
    app.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
