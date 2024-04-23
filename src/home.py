import tkinter as tk
from tkinter import ttk
from carousel import CarouselSlider
from PIL import Image, ImageTk
from booking import BookingInterface
from mybookings import MyBookings
class HomeApp(tk.Frame):
    def __init__(self, master,username):
        super().__init__(master)
        self.master = master
        self.master.title("Home")
        self.configure(background="#f3f3f3")
        self.master.state('zoomed')
        self.username = username
        self.init_ui()

    def init_ui(self):
        self.pack(expand=True, fill=tk.BOTH)

        # Creating frames
        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='y',side='left')

        # Create CarouselSlider
        self.carousel = CarouselSlider(self.frame1)
        self.carousel.pack()

        self.frame2 = tk.Frame(self)
        self.frame2.pack(fill='y', side='left',padx=10)
        # self.frame2.config(bg="yellow")

        self.frame3 = tk.Frame(self,bg='#D1F7FF')
        self.frame3.pack(fill='both', expand=True)
        self.booking_frame = None
        self.car_frame = None
        self.bike_frame = None
        self.ev_frame = None
        self.sports_frame = None
        self.royalenfield_frame = None
        

        # Widgets for frame 2
        self.select_vehicle_frame = tk.Frame(self.frame2)
        self.select_vehicle_frame.pack(fill='y')
        # self.select_vehicle_frame.config(bg="yellow")

        tk.Label(self.select_vehicle_frame,padx=25,pady=30, text="Select vehicle type:", font=('Helvetica', 25,'bold')).pack()
        self.vehicle_var = tk.StringVar()
        self.vehicle_var.set("Cars")  # Default selection
        
        tk.Radiobutton(self.select_vehicle_frame,padx=25,pady=5 ,text="Cars", variable=self.vehicle_var, value="Cars",font=('Helvetica', 15,'bold'), command=self.populate_frames).pack(anchor='w')
        
        tk.Radiobutton(self.select_vehicle_frame,padx=25,pady=5, text="Bikes", variable=self.vehicle_var, value="Bikes",font=('Helvetica', 15,'bold'), command=self.populate_frames).pack(anchor='w')
        
        tk.Radiobutton(self.select_vehicle_frame,padx=25,pady=5, text="EV Cars", variable=self.vehicle_var, value="EV Cars",font=('Helvetica', 15,'bold'), command=self.populate_frames).pack(anchor='w')
        
        tk.Radiobutton(self.select_vehicle_frame,padx=25,pady=5, text="EV Bikes", variable=self.vehicle_var, value="EV Bikes",font=('Helvetica', 15,'bold'), command=self.populate_frames).pack(anchor='w')

        tk.Radiobutton(self.select_vehicle_frame,padx=25,pady=5, text="Sports Bikes", variable=self.vehicle_var, value="Sports Bikes",font=('Helvetica', 15,'bold'), command=self.populate_frames).pack(anchor='w')

        tk.Radiobutton(self.select_vehicle_frame,padx=25,pady=5, text="Royal Enfields", variable=self.vehicle_var, value="Royal Enfields",font=('Helvetica', 15,'bold'), command=self.populate_frames).pack(anchor='w')

        self.bookings_button = tk.Button(self.frame2, width=15, text='My Bookings', bg='#57a1f8', fg='white', border=0,font=('Microsoft YaHei UI Light', 14),command=self.show_mybookings)
        # self.bookings_button.pack(anchor=tk.CENTER,pady=20,padx=10)
        self.bookings_button.place(x=100,y=500)

        self.logout_button = tk.Button(self.frame2, width=15, text='Log Out', bg='#57a1f8', fg='white', border=0,font=('Microsoft YaHei UI Light', 14),command=self.show_login)
        # self.logout_button.pack(anchor=tk.CENTER,pady=20,padx=10)
        self.logout_button.place(x=100,y=580)

        # Initially populate frames based on selection
        self.populate_frames()

    def show_login(self):
        self.destroy()
        from login import LoginWindow
        login_frame = LoginWindow(self.master)
        login_frame.pack(expand=True, fill=tk.BOTH)

    def populate_frames(self):
        # Hide frames when selecting vehicle type
        if self.car_frame:
            self.car_frame.destroy()

        if self.bike_frame:
            self.bike_frame.destroy()

        if self.ev_frame:
            self.ev_frame.destroy()

        if self.sports_frame:
            self.sports_frame.destroy()
        
        if self.royalenfield_frame:
            self.royalenfield_frame.destroy()

        if self.vehicle_var.get() == "Cars":
            self.populate_cars()

        elif self.vehicle_var.get() == "Bikes":
            self.populate_bikes()

        elif self.vehicle_var.get() == "EV Cars":
            self.populate_ev_cars()

        elif self.vehicle_var.get() == "EV Bikes":
            self.populate_ev_bikes()

        elif self.vehicle_var.get() == "Sports Bikes":
            self.populate_sports_bikes()
        
        elif self.vehicle_var.get() == "Royal Enfields":
            self.populate_royal_enfields()

    def populate_cars(self):
        self.car_frame = ttk.Frame(self.frame3)
        self.car_frame.pack(fill='both', expand=True)

        # Clear previous content
        for widget in self.car_frame.winfo_children():
            widget.destroy()
        
        cars = [
            {"name": "Maruti Suzuki Swift",
              "image": "./super-x/assets/swift.jpg",
              "engine": "Petrol", 
              "transmission": "Manual", 
              "rent": "₹91"},

              {"name": "Mahindra Scorpio N", 
             "image": "./super-x/assets/scorpion.jpg", 
             "engine": "Diesel", 
             "transmission": "Manual", 
             "rent": "₹181"},

             {"name": "Maruti Suzuki Fronx", 
             "image": "./super-x/assets/fronx.jpg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹105"},

            {"name": "Hyundai Exter", 
             "image": "./super-x/assets/exter.jpg", 
             "engine": "Petrol", 
             "transmission": "Automatic", 
             "rent": "₹75"},

            {"name": "Maruti Suzuki Brezza", 
             "image": "./super-x/assets/brezza.jpg", 
             "engine": "Diesel", 
             "transmission": "Manual", 
             "rent": "₹94"},

            {"name": "Tata Tiago", 
             "image": "./super-x/assets/tiago.jpg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹76"},   

            {"name": "Renault Kwid", 
             "image": "./super-x/assets/kwid.jpg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹82"},

             {"name": "Hyundai Grand ilO", 
             "image": "./super-x/assets/i10.jpg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹72"},
            
            {"name": "Tata Nexon", 
             "image": "./super-x/assets/nexon.jpg", 
             "engine": "Diesel", 
             "transmission": "Automatic", 
             "rent": "₹116"},
            
            {"name": "Maruti Suzuki Swift Dzire", 
             "image": "./super-x/assets/dzire.jpg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹104"} 
             ]
        
        self.populate_vehicle_frame(self.car_frame, cars)
    
    def populate_royal_enfields(self):
        self.royalenfield_frame = ttk.Frame(self.frame3)
        self.royalenfield_frame.pack(fill='both', expand=True)

        # Clear previous content
        for widget in self.royalenfield_frame.winfo_children():
            widget.destroy()
        
        royalenfields = [
            {"name": "Royal Enfield Hunter 350",
              "image": "./super-x/assets/RoyalEnfields/hunter350.png",
              "engine": "Petrol", 
              "transmission": "Manual", 
              "rent": "₹91"},

              {"name": "Royal Enfield Continental GT 650", 
             "image": "./super-x/assets/RoyalEnfields/continentalgt650.png", 
             "engine": "Diesel", 
             "transmission": "Manual", 
             "rent": "₹181"},

             {"name": "Royal Enfield Bullet 350", 
             "image": "./super-x/assets/RoyalEnfields/bullet350.png", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹105"},

            {"name": "Royal Enfield Classic 350", 
             "image": "./super-x/assets/RoyalEnfields/classic350.jpeg", 
             "engine": "Petrol", 
             "transmission": "Automatic", 
             "rent": "₹75"},

            {"name": "Royal Enfield Shotgun 650", 
             "image": "./super-x/assets/RoyalEnfields/shotgun650.jpeg", 
             "engine": "Diesel", 
             "transmission": "Manual", 
             "rent": "₹94"},

            {"name": "Royal Enfield Meteor 350", 
             "image": "./super-x/assets/RoyalEnfields/meteor350.jpeg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹76"},   

            {"name": "Royal Enfield Himalayan 450", 
             "image": "./super-x/assets/RoyalEnfields/himalayan450.jpeg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹82"},
 
             ]
        
        self.populate_vehicle_frame(self.royalenfield_frame, royalenfields)

    def populate_ev_cars(self):
        self.ev_frame = ttk.Frame(self.frame3)
        self.ev_frame.pack(fill='both', expand=True)

        # Clear previous content
        for widget in self.ev_frame.winfo_children():
            widget.destroy()

        ev_cars = [

             {"name": "MG Comet EV", 
             "image": "./super-x/assets/cometev.jpg", 
             "engine": "Electric", 
             "transmission": "Manual", 
             "rent": "₹84"},
            
             {"name": "Tata Tiago EV", 
             "image": "./super-x/assets/tiagoev.jpg", 
             "engine": "Electric", 
             "transmission": "Automatic", 
             "rent": "₹104"},

            {"name": "Tata Punch EV", 
             "image": "./super-x/assets/punchev.jpg", 
             "engine": "Electric", 
             "transmission": "Manual", 
             "rent": "₹94"},
             
             {"name": "Citroen eC3", 
             "image": "./super-x/assets/ec3ev.jpg", 
             "engine": "Electric", 
             "transmission": "Automatic", 
             "rent": "₹104"},

             {"name": "Tata Nexon EV", 
             "image": "./super-x/assets/nexonev.jpg", 
             "engine": "Electric", 
             "transmission": "Manual", 
             "rent": "₹104"},

             {"name": "Mahindra XUV400 EV", 
             "image": "./super-x/assets/xuv400ev.jpg", 
             "engine": "Electric", 
             "transmission": "Automatic", 
             "rent": "₹104"},

             {"name": "BYD Atto 3 EV", 
             "image": "./super-x/assets/atto3ev.jpg", 
             "engine": "Electric", 
             "transmission": "Automatic", 
             "rent": "₹104"},

             {"name": "MG ZS EV", 
             "image": "./super-x/assets/zsev.jpg", 
             "engine": "Electric", 
             "transmission": "Manual", 
             "rent": "₹104"},

             {"name": "Tata Altroz EV", 
             "image": "./super-x/assets/altrozev.jpg", 
             "engine": "Electric", 
             "transmission": "Manual", 
             "rent": "₹104"}
             ]
        
        self.populate_vehicle_frame(self.ev_frame, ev_cars) 

    def populate_bikes(self):
        self.bike_frame = ttk.Frame(self.frame3)
        self.bike_frame.pack(fill='both', expand=True)

        # Clear previous content
        for widget in self.bike_frame.winfo_children():
            widget.destroy()

        bikes = [
            {"name": "TVS Raider 125", 
             "image": "./super-x/assets/raider.png", 
             "engine": "125cc", 
             "transmission": "Manual", 
             "rent": "₹94"},
             
            {"name": "Honda SP 125", 
             "image": "./super-x/assets/sp.jpg", 
             "engine": "125cc", 
             "transmission": "Manual", 
             "rent": "₹94"},

            {"name": "Hero Splendor Plus", 
             "image": "./super-x/assets/splendorplus.png", 
             "engine": "100cc", 
             "transmission": "Automatic", 
             "rent": "₹94"},

             {"name": "Yamaha FZS V4", 
             "image": "./super-x/assets/fz.png", 
             "engine": "125cc", 
             "transmission": "Manual", 
             "rent": "₹94"},
            
             ]
        
        self.populate_vehicle_frame(self.bike_frame, bikes) 

    def populate_ev_bikes(self):
        self.ev_frame = ttk.Frame(self.frame3)
        self.ev_frame.pack(fill='both', expand=True)

        # Clear previous content
        for widget in self.ev_frame.winfo_children():
            widget.destroy()

        ev_bikes = [
            {"name": "Revolt RV 400", 
             "image": "./super-x/assets/rv400.jpg", 
             "engine": "Electric", 
             "transmission": "Automatic", 
             "rent": "₹30"},
             
            {"name": "Tork Kratos R", 
             "image": "./super-x/assets/kratos.jpg", 
             "engine": "Electric", 
             "transmission": "Automatic", 
             "rent": "₹35"},

            {"name": "Bajaj Chetak", 
             "image": "./super-x/assets/chetak.png", 
             "engine": "Electric", 
             "transmission": "Automatic", 
             "rent": "₹40"}

             ]
        self.populate_vehicle_frame(self.ev_frame, ev_bikes)

    def populate_sports_bikes(self):
        self.sports_frame = ttk.Frame(self.frame3)
        self.sports_frame.pack(fill='both', expand=True)

        # Clear previous content
        for widget in self.sports_frame.winfo_children():
            widget.destroy()

        sports_bikes = [
            {"name": "BMW G310 RR", 
             "image": "./super-x/assets/SportsBikes/bmw.jpg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹30"},

            {"name": "Suzuki Hayabusa", 
             "image": "./super-x/assets/SportsBikes/hayabusa.jpg", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹30"},
            
            {"name": "Kawasaki Ninja H2R", 
             "image": "./super-x/assets/SportsBikes/ninja.png", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹30"},
            
            {"name": "Yamaha MT15", 
             "image": "./super-x/assets/SportsBikes/mt15.png", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹30"},

             {"name": "Bajaj Pulsar 200", 
             "image": "./super-x/assets/SportsBikes/pulsar200.png", 
             "engine": "Petrol", 
             "transmission": "Manual", 
             "rent": "₹30"}
             
             ]
        
        self.populate_vehicle_frame(self.sports_frame, sports_bikes)

    def populate_vehicle_frame(self, parent_frame, vehicle_list):
        # Create a canvas within a frame to hold the vehicle information
        canvas = tk.Canvas(parent_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(parent_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        for i, vehicle in enumerate(vehicle_list):
            vehicle_frame = ttk.Frame(inner_frame)
            vehicle_frame.grid(row=i, column=0, padx=20, pady=10, sticky='w')
            vehicle_image = Image.open(vehicle["image"])  # Image path
            vehicle_image = vehicle_image.resize((350, 175))
            vehicle_photo = ImageTk.PhotoImage(vehicle_image)
            vehicle_label = ttk.Label(vehicle_frame, image=vehicle_photo)
            vehicle_label.image = vehicle_photo
            vehicle_label.grid(rowspan=5,row=0, column=0)

            vehicle_name = ttk.Label(vehicle_frame, text=vehicle["name"], font=('Helvetica', 14, 'bold'))
            vehicle_name.grid(row=0, column=1, sticky='w',padx=25)

            vehicle_details = ttk.Label(vehicle_frame, text=f"Engine Type: {vehicle['engine']}", font=('Helvetica', 10,'bold'))
            vehicle_details.grid(row=1, column=1, sticky='w',padx=25)

            vehicle_rent = ttk.Label(vehicle_frame, text=f"Transmission Type: {vehicle['transmission']}", font=('Helvetica', 10,'bold'))
            vehicle_rent.grid(row=2, column=1, sticky='w',padx=25)

            vehicle_rent = ttk.Label(vehicle_frame, text=f"Rent per hour: {vehicle['rent']}", font=('Helvetica', 10,'bold'))
            vehicle_rent.grid(row=3, column=1, sticky='w',padx=25)

            book_button = tk.Button(vehicle_frame,cursor='hand2',border=0, text="Book Now", command=lambda v=vehicle: self.book_now(v),fg='#57a1f8',font=('Helvetica', 14,'bold'))
            book_button.grid(row=4, column=1, sticky='w',padx=25)


        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Mousepad scrolling functionality
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)

    def book_now(self, vehicle_info):
        if self.booking_frame:
            self.booking_frame.destroy()
            
        booking_frame = BookingInterface(self, vehicle_info,self.username)
        booking_frame.pack_propagate()

    def show_mybookings(self):
        my_bookings_window = MyBookings(self.master, self.username)

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("RentWheels")
    home_app = HomeApp(root,"Pranav407")
    home_app.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
