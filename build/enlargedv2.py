from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Downloads\Tkinter-Designer\build\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

current_scale = 1

def enlarge_image():
    global current_scale

    current_scale += 0.1  # Increase the scale factor
    render_image()

def render_image():
    global original_image
    global image_label

    image = original_image.copy()
    image = image.resize((int(image.width * current_scale), int(image.height * current_scale)))
    photo = ImageTk.PhotoImage(image=image)

    image_label.config(image=photo)
    image_label.image = photo

window = Tk()
window.geometry("620x400")

canvas = Canvas(
    window,
    height=400,
    width=620,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
original_image = Image.open(relative_to_assets("image_1.png"))

image_label = tk.Label(window, image=image_image_1)
image_label.image = image_image_1
image_label.pack()

image_2 = canvas.create_image(310.0, 190.0, image=image_image_1)
image.pack()

enlarge_button = tk.Button(window, text="Enlarge", command=enlarge_image)
enlarge_button.pack()

window.mainloop()
