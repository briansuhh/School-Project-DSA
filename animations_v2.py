import tkinter as tk
from PIL import Image, ImageTk
import os

# Create the main window
root = tk.Tk()
root.title("Image Animation")
root.geometry("500x500")

# Create a canvas to display the animation
canvas = tk.Canvas(root, width=100, height=100, background="grey")
canvas.pack()

# Folder containing image files
image_folder = "light"

# Get a list of image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

print(image_files)

# # Sort the image files in alphabetical order
# image_files.sort()

# Create a list to store ImageTk PhotoImage objects
image_list = []

# Load image files and convert them to PhotoImage
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_list.append(photo)

frame_index = 0

def update_frame():
    global frame_index
    if frame_index < len(image_list):
        frame = image_list[frame_index]
        
        # Display the current frame
        canvas.create_image(0, 0, anchor=tk.NW, image=frame)
        
        # Increment the frame index
        frame_index += 1

        # Repeat this function after a delay for the animation effect
        canvas.after(100, update_frame)
    else:
        # All images have been displayed, so stop the loop
        frame_index = 0

# Start the animation
update_frame()

# Run the main event loop
root.mainloop()
