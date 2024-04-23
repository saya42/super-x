import tkinter as tk
from landing import LandingPage

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RentWheels")
        self.state('zoomed')
        self.configure(background="White")
        self.show_landing_page()

    def show_landing_page(self):
        landing_page = LandingPage(self)
        landing_page.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()