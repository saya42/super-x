# mybookings.py

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from firebase_admin import firestore

class MyBookings(tk.Toplevel):
    def __init__(self, master, username):
        super().__init__(master)
        self.title("My Bookings")
        self.state('zoomed')
        self.username = username
        self.configure(bg="#f3f3f3")

        # Create a canvas and scrollbar
        self.canvas = tk.Canvas(self, bg="#f3f3f3")
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.display_bookings()
        
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def display_bookings(self):
        # Fetch bookings from Firestore for the current user
        bookings_ref = firestore.client().collection("Bookings").document(self.username).collection("bookings")
        bookings = bookings_ref.get()

        if not bookings:
            ttk.Label(self.scrollable_frame, text="No bookings found.", font=('Helvetica', 16, 'bold')).pack(pady=20)
            return

        for i, booking in enumerate(bookings):
            booking_data = booking.to_dict()

            vehicle_name = booking_data["Vehicle Name"]

            pickdate = booking_data["Pickup Date"]
            picktime = booking_data["Pickup Time"]

            dropdate = booking_data["Drop Date"]
            droptime = booking_data["Drop Time"]

            location = booking_data["Location"]

            rental_fee = booking_data["Total Payment"]

            vehicle_image_path = booking_data.get("Vehicle Image Path", "")

            # Create a frame for each booking
            booking_frame = ttk.Frame(self.scrollable_frame, padding=10, relief=tk.RAISED, borderwidth=2)
            booking_frame.pack(pady=20, padx=50, fill=tk.BOTH)

            ttk.Label(booking_frame, text=f"Booking {i+1}", font=('Helvetica', 18, 'bold')).grid(row=0, column=0, columnspan=2)

            ttk.Label(booking_frame, text=f"Vehicle Name: {vehicle_name}", font=('Helvetica', 14)).grid(row=1, column=0, sticky='w', pady=5)

            ttk.Label(booking_frame, text=f"Pickup Date: {pickdate}", font=('Helvetica', 14)).grid(row=2, column=0, sticky='w', pady=5)

            ttk.Label(booking_frame, text=f"Pickup Time: {picktime}", font=('Helvetica', 14)).grid(row=3, column=0, sticky='w', pady=5)

            ttk.Label(booking_frame, text=f"Drop Date: {dropdate}", font=('Helvetica', 14)).grid(row=4, column=0, sticky='w', pady=5)

            ttk.Label(booking_frame, text=f"Drop Time: {droptime}", font=('Helvetica', 14)).grid(row=5, column=0, sticky='w', pady=5)

            ttk.Label(booking_frame, text=f"Location: {location}", font=('Helvetica', 14)).grid(row=6, column=0, sticky='w', pady=5)
            
            ttk.Label(booking_frame, text=f"Total Payment: ₹{rental_fee:.2f}", font=('Helvetica', 14)).grid(row=7, column=0, sticky='w', pady=5)

            # Load and display the vehicle image
            if vehicle_image_path:
                vehicle_image = Image.open(vehicle_image_path)
                vehicle_image = vehicle_image.resize((500, 250))  # Resize the image as needed
                vehicle_photo = ImageTk.PhotoImage(vehicle_image)
                vehicle_image_label = ttk.Label(booking_frame, image=vehicle_photo)
                vehicle_image_label.image = vehicle_photo  # Keep a reference to avoid garbage collection
                vehicle_image_label.grid(row=1, column=1, rowspan=9, padx=30)

            # Add a cancel booking button
            cancel_button = ttk.Button(booking_frame, text="Cancel Booking", command=lambda idx=i: self.cancel_booking(idx))
            cancel_button.grid(row=8, column=0, pady=10)

    def cancel_booking(self, idx):
        # Delete the booking from Firestore
        bookings_ref = firestore.client().collection("Bookings").document(self.username).collection("bookings")
        bookings = bookings_ref.get()
        booking_id = bookings[idx].id
        bookings_ref.document(booking_id).delete()
        # Refresh the window to reflect changes
        self.destroy()
        MyBookings(self.master, self.username)
