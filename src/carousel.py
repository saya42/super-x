# carousel_slider.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CarouselSlider(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.image_paths = [
            "./super-x/assets/1.png",
            "./super-x/assets/2.png",
            "./super-x/assets/3.png",
            "./super-x/assets/4.png",
            ]
        self.current_index = 0

        self.image_label = tk.Label(self)
        self.image_label.pack(expand=True, fill='both')

        self.load_image()
        self.after(3000, self.next_image)

    def load_image(self):
        image_path = self.image_paths[self.current_index]
        image = Image.open(image_path)
        image = image.resize((450, 800))
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.load_image()
        self.after(3000, self.next_image)

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    app = CarouselSlider(root)
    root.mainloop()