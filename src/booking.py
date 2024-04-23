import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase
cred = credentials.Certificate("./super-x/setup/super-x.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

class BookingInterface(tk.Toplevel):
    
    def __init__(self, master, vehicle_info,username):
        super().__init__(master)
        self.title("Booking")
        self.state('zoomed')
        # Define custom colors
        bg_color = "#f0f0f0"
        text_color = "#333333"
        accent_color = "#007bff"
        self.username = username
        self.configure(bg=bg_color)
        self.vehicle_info = vehicle_info
        self.selected_hours = tk.IntVar(value=1)  # Default to 1 hour
        self.trip_protection_var = tk.StringVar(value="Basic")  # Default trip protection package

        # Display the selected vehicle image
        self.display_vehicle_image()

        # Selected Vehicle Section
        tk.Label(self, text="Selected Vehicle:", font=('Helvetica', 20, 'bold'), foreground=accent_color).place(x=10,y=390)

        ttk.Label(self, text=f"Vehicle Name: {vehicle_info['name']}", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=10,y=445)

        ttk.Label(self, text=f"Engine Type: {vehicle_info['engine']}", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=10,y=485)

        ttk.Label(self, text=f"Transmission Type: {vehicle_info['transmission']}", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=10,y=525)

        ttk.Label(self, text=f"Rent per hour: {vehicle_info['rent']}", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=10,y=565)

        ttk.Label(self, text="Enter your Name :", font=('Helvetica', 16,'bold'), foreground=text_color,width=200).place(x=660,y=20)
        self.name_entry = ttk.Entry(self)
        self.name_entry.place(x=860,y=20)

        ttk.Label(self, text="Pickup Date:", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=660,y=70)

        self.pickup_date_entry = DateEntry(self, date_pattern='dd-mm-yyyy')
        self.pickup_date_entry.place(x=800,y=70)

        ttk.Label(self, text="Pickup Time:", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=660,y=130)
        
        self.pickup_time_var = tk.StringVar(value="00:00")
        self.pickup_time_dropdown = ttk.Combobox(self, textvariable=self.pickup_time_var, values=self.generate_time_options(), width=10)
        self.pickup_time_dropdown.place(x=800,y=130)

        ttk.Label(self, text="Drop Date:", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=950,y=70)

        self.drop_date_entry = DateEntry(self, date_pattern='dd-mm-yyyy')
        self.drop_date_entry.place(x=1075,y=70)

        ttk.Label(self, text="Drop Time:", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=950,y=130)

        self.drop_time_var = tk.StringVar(value="00:00")
        self.drop_time_dropdown = ttk.Combobox(self, textvariable=self.drop_time_var, values=self.generate_time_options(), width=10)
        self.drop_time_dropdown.place(x=1075,y=130)

        ttk.Label(self, text="Location:", font=('Helvetica', 16, 'bold'), foreground=text_color).place(x=660,y=190)
        self.location_entry = ttk.Entry(self)
        self.location_entry.place(x=800,y=190)

        ttk.Label(self, text="Trip Protection Packages:", font=('Helvetica', 16, 'bold'), foreground=accent_color).place(x=660,y=260)

        # Increase font size and padding for Radiobutton
        style = ttk.Style()
        style.configure("TRadiobutton", font=("Helvetica", 14))

        ttk.Radiobutton(self, text="Basic", variable=self.trip_protection_var, value="Basic").place(x=680,y=300)

        ttk.Radiobutton(self, text="Standard", variable=self.trip_protection_var, value="Standard").place(x=680,y=340)
        
        ttk.Radiobutton(self, text="Premium", variable=self.trip_protection_var, value="Premium").place(x=680,y=380)

        self.calculate_total_button = tk.Button(self, text="Calculate Total Payment", command=self.calculate_payment,width=20,border=0,bg='#f0f0f0',fg="#007bff",font=('Helvetica', 14,'bold'),cursor='hand2')
        self.calculate_total_button.place(x=660,y=450)

        self.total_payment_label = ttk.Label(self, text="", font=('Helvetica', 14), foreground='black')
        self.total_payment_label.place(x=675,y=500)
        
        self.payment_summary_button = tk.Button(self, text="Payment Summary", command=self.show_payment_summary,width=20,bg='#f0f0f0',fg="#007bff",border=0,font=('Helvetica', 16, 'bold'))
        self.payment_summary_button.place(x=1080,y=255)

        tk.Button(self, text="Book Now",bg='#f0f0f0',fg="#007bff",border=0, command=self.book_now,width=10,font=('Helvetica', 16, 'bold')).place(x=680,y=550)

        # Create a "Back" button
        tk.Button(self, text="Back",bg='#f0f0f0',fg="#007bff", command=self.go_back,width=10,border=0,font=('Helvetica', 16, 'bold')).place(x=1090,y=550)

    def go_back(self):
        # Destroy the current booking interface
        self.destroy()
        

    def book_now(self):

        username = self.username
        name = self.name_entry.get()
        pickup_date = self.pickup_date_entry.get()
        pickup_time = self.pickup_time_var.get()
        drop_date = self.drop_date_entry.get()
        drop_time = self.drop_time_var.get()
        location = self.location_entry.get()
        trip_protection = self.trip_protection_var.get()

        total_payment_text = self.total_payment_label.cget("text")
        total_payment = float(total_payment_text.split("₹")[-1])

        vehicle_name = self.vehicle_info["name"]
        
        vehicle_image_path = self.vehicle_info["image"]
        
        # Create a dictionary for the booking data
        booking_data = {
            "Name": name,
            "Vehicle Name": vehicle_name,
            "Vehicle Image Path": vehicle_image_path,
            "Pickup Date": pickup_date,
            "Pickup Time": pickup_time,
            "Drop Date": drop_date,
            "Drop Time": drop_time,
            "Location": location,
            "Trip Protection": trip_protection,
            "Total Payment": total_payment
        }

        # Get the number of existing bookings for the user
        user_ref = db.collection("Bookings").document(username)
        bookings_ref = user_ref.collection("bookings")
        num_bookings = len(bookings_ref.get())

        # Create a new booking with a document name like "booking 1", "booking 2", etc.
        new_booking_ref = bookings_ref.document(f"booking {num_bookings + 1}")
        new_booking_ref.set(booking_data)

        # # Add booking data to Firestore
        doc_ref = db.collection("booking_info").document(name)
        doc_ref.set(booking_data)

        messagebox.showinfo("Booking", "Your booking has been confirmed!")

        self.destroy()

    def show_payment_summary(self):
        
        rent_per_hour = float(self.vehicle_info['rent'].replace('₹', '').strip())
        pickup_time = self.pickup_time_var.get()
        drop_time = self.drop_time_var.get()
        pickup_datetime = datetime.combine(self.pickup_date_entry.get_date(), datetime.strptime(pickup_time, '%H:%M').time())
        drop_datetime = datetime.combine(self.drop_date_entry.get_date(), datetime.strptime(drop_time, '%H:%M').time())
        total_hours = (drop_datetime - pickup_datetime).total_seconds() / 3600

        rental_fee = rent_per_hour * total_hours
        trip_protection_fee = self.calculate_trip_protection_amount()
        convenience_fee = 100
        total_payment = rental_fee + trip_protection_fee + convenience_fee

        summary_text = f"Rental Fee: ₹{rental_fee:.2f}\n\nTrip Protection Fee: ₹{trip_protection_fee:.2f}\n\nConvenience Fee: ₹{convenience_fee:.2f}\n\nTotal Payment: ₹{total_payment:.2f}"
        
        self.total_summary_label = ttk.Label(self, text="", font=('Helvetica', 14), foreground='black')
        self.total_summary_label.place(x=1120,y=315)

        self.total_summary_label.config(text=summary_text)
        
        # messagebox.showinfo("Payment Summary", summary_text)

    def calculate_trip_protection_amount(self):

        if self.trip_protection_var.get() == "Basic":
            return 50
        elif self.trip_protection_var.get() == "Standard":
            return 100
        elif self.trip_protection_var.get() == "Premium":
            return 150
        
    def calculate_payment(self):
        rent_per_hour = float(self.vehicle_info['rent'].replace('₹', '').strip())

        pickup_time = self.pickup_time_var.get()
        drop_time = self.drop_time_var.get()

        pickup_datetime = datetime.combine(self.pickup_date_entry.get_date(), datetime.strptime(pickup_time, '%H:%M').time())
        drop_datetime = datetime.combine(self.drop_date_entry.get_date(), datetime.strptime(drop_time, '%H:%M').time())

        total_hours = (drop_datetime - pickup_datetime).total_seconds() / 3600

        total_payment = rent_per_hour * total_hours
        # Add trip protection package amount and convenience fee
        total_payment += self.calculate_trip_protection_amount() + 100
        self.total_payment_label.config(text=f"Total Payment: ₹{total_payment:.2f}")

    def generate_time_options(self):
        times = []
        for hour in range(0, 24):
            for minute in range(0, 60, 60):  # Increment by 30 minutes
                time_string = f"{hour:02d}:{minute:02d}"
                times.append(time_string)
        return times

    def display_vehicle_image(self):
        # Load the selected vehicle image
        vehicle_image = Image.open(self.vehicle_info["image"])
        vehicle_image = vehicle_image.resize((600, 350))  # Resize the image as needed
        self.vehicle_photo = ImageTk.PhotoImage(vehicle_image)

        # Create a label to display the image
        vehicle_image_label = ttk.Label(self, image=self.vehicle_photo)
        vehicle_image_label.image = self.vehicle_photo  # Keep a reference to avoid garbage collection
        vehicle_image_label.place(x=0,y=0)


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    vehicle_info = {
        "name": "Car",
        "engine": "V8",
        "transmission": "Automatic",
        "rent": "₹50",
        "image": "./super-x/assets/thar.jpg"
    }
    BookingInterface(root, vehicle_info,"Shru")
    root.mainloop()