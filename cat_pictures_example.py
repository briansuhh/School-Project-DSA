import tkinter as tk
from PIL import Image, ImageTk
import csv
import customtkinter as ctk

# Create a tkinter window
root = tk.Tk()
root.title("Display Pictures from CSV")

# Create a Canvas to display images
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Read the CSV file using pandas
data = []
with open("image_data.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Function to display pictures
def display_pictures():
    for item in data:
        image = Image.open(item["image_path"])
        photo = ImageTk.PhotoImage(image)
        image_button = ctk.CTkButton(adopt_frame, text="", image=photo, width=100, height=100, fg_color="transparent", hover_color="grey")
        image_button.configure(command=lambda img=image: cat_button_event(img["image_path"]))  # Example event handler
        image_button.pack(side=tk.LEFT, padx=10, pady=10)
        image_button.photo = photo  # Keep a reference to prevent garbage collection

# Call the function to start displaying pictures
display_pictures()

# Start the main loop
root.mainloop()
