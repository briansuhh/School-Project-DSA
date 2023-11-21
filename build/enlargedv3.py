import tkinter as tk
from PIL import Image, ImageTk

original_image = None

current_scale = 1  # The current scale factor


# Function to enlarge the image
def enlarge_image():
    global image_label, current_scale

    current_scale += 1  # Increase the scale factor
    image_1 = Image.open("assets/frame1/image_1.png")
    image = image_1.copy()
    image = image.resize((int(image.width * current_scale), int(image.height * current_scale)))
    photo = ImageTk.PhotoImage(image=image)

    image_label.config(image=photo)
    image_label.image = photo

# Create the main window
root = tk.Tk()
root.title("Image Enlarger App")

image_1 = Image.open("build/assets/frame1/image_1.png")
image_2 = Image.open("build/assets/frame1/image_2.png")

image_1 = ImageTk.PhotoImage(image=image_1)
image_2 = ImageTk.PhotoImage(image=image_2)

# Create a label to display the image
image_label = tk.Label(root, image=image_1)
image_label.pack()

image_label2 = tk.Label(root, image=image_2)
image_label2.pack()

image_label

# Create a button to enlarge the image
enlarge_button = tk.Button(root, text="Enlarge", command=enlarge_image)
enlarge_button.pack()

root.mainloop()
