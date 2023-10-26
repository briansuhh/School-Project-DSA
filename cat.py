from customtkinter import *
import tkinter as tk
from tkinter import messagebox

# Initialize lists to store cat information and adoption records
cat_data = []
adoption_records = []

# Function to add a new cat
def add_cat():
    name = cat_name_entry.get()
    description = cat_description_entry.get()
    age = cat_age_entry.get()
    photo = cat_photo_entry.get()
    
     # Check if any of the cat's information is missing
    if not (name and description and age and photo):
        messagebox.showerror("Incomplete Cat Profile", "Please provide all cat information.")
    else:
        cat_data.append({
            "Name": name,
            "Description": description,
            "Age": age,
            "Photo": photo
        })
    
    # Clear the input fields
    cat_name_entry.delete(0, tk.END)
    cat_description_entry.delete(0, tk.END)
    cat_age_entry.delete(0, tk.END)
    cat_photo_entry.delete(0, tk.END)

    # Display the added cat in the listbox
    cat_listbox.insert(tk.END, name)

# Function to display cat details
def show_cat_details(event):
    selected_index = cat_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        selected_cat = cat_data[index]
        cat_details_label.configure(text=f"Name: {selected_cat['Name']}\n"
                                     f"Description: {selected_cat['Description']}\n"
                                     f"Age: {selected_cat['Age']}\n"
                                     f"Photo: {selected_cat['Photo']}")

# Function to mark a cat for adoption
def mark_for_adoption():
    selected_index = cat_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        selected_cat = cat_data.pop(index)
        adoption_records.append(selected_cat)
        cat_listbox.delete(index)

# Create the main application window
app = CTk()
app.title("Cat Adoption Center")
app.geometry("500x500") 

# Create input fields
cat_name_label = CTkLabel(app, text="Cat Name:")
cat_name_label.pack()
cat_name_entry = CTkEntry(app)
cat_name_entry.pack()

cat_description_label = CTkLabel(app, text="Description:")
cat_description_label.pack()
cat_description_entry = CTkEntry(app)
cat_description_entry.pack()

cat_age_label = CTkLabel(app, text="Age:")
cat_age_label.pack()
cat_age_entry = CTkEntry(app)
cat_age_entry.pack()

cat_photo_label = CTkLabel(app, text="Photo URL:")
cat_photo_label.pack()
cat_photo_entry = CTkEntry(app)
cat_photo_entry.pack()

add_button = CTkButton(app, text="Add Cat", command=add_cat)
add_button.pack()

# Create a listbox to display cat names
cat_listbox = tk.Listbox(app, selectmode=tk.SINGLE)
cat_listbox.pack()
cat_listbox.bind('<<ListboxSelect>>', show_cat_details)

# Create a label to display cat details
cat_details_label = CTkLabel(app, text="")
cat_details_label.pack()

# Create buttons for marking for adoption
mark_for_adoption_button = CTkButton(app, text="Mark for Adoption", command=mark_for_adoption)
mark_for_adoption_button.pack()

# Start the Tkinter main loop
app.mainloop()
