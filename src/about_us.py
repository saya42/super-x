import tkinter as tk

class Aboutus(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("About Us")
        self.master.state('zoomed')
        self.img_path = "./super-x/assets/about.png"
        self.img = tk.PhotoImage(file=self.img_path)
        tk.Label(self.master, image=self.img, bg='#fff').pack()

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    app = Aboutus()
    app.run()
