from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Downloads\Tkinter-Designer\build\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def enlarge_image():
    canvas.itemconfig(image_1, image=image_image_2)  # Change the image to the larger one

window = Tk()
window.geometry("620x400")
window.configure()


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
image_1 = canvas.create_image(310.0, 190.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("enlarged.png"))  # An enlarged version of image_1

enlarge_button = tk.Button(window, text="Enlarge", command=enlarge_image)
enlarge_button.pack()

window.mainloop()
