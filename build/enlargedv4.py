from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk

current_scale = 1  # The current scale factor
target_scale = 3  # The target scale factor
step = 0.1  # The step size for scaling

def enlarge_image():
    global image_label, current_scale

    if current_scale < target_scale:
        current_scale += step
        image = pic_1.copy()
        image = image.resize((int(image.width * current_scale), int(image.height * current_scale)))
        photo = ImageTk.PhotoImage(image=image)

        image_label.config(image=photo)
        image_label.image = photo
        window.after(50, enlarge_image)

window = Tk()
window.geometry("620x400")
window.configure(bg="#FFFFFF")

pic_1 = Image.open("build/assets/frame1/image_1.png")
image_1 = ImageTk.PhotoImage(image=pic_1)

image_label = Label(window, image=image_1, bg="#F6F4C6")
image_label.place(relx=0.5, rely=0.5, anchor="center")

enlarge_image()
window.resizable(False, False)
window.mainloop()
