import customtkinter as ctk
from customtkinter import *
import pandas as pd
from PIL import Image

# Open the CSV file that will act as the database for the credentials
df = pd.read_csv('credentials.csv')

# Create a list of usernames and passwords from the CSV file
usernames = df['username'].tolist()
passwords = df['password'].tolist()

def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # # Check if the username and password entered match the ones in the CSV file
    # if entered_username in usernames and entered_password in passwords:
    #     result_label.configure(text="Login Successful")
    #     # if successful, hide login_page and display homepage
    #     login_page.pack_forget()
    #     homepage.pack(fill="both", expand=True, anchor=CENTER)
    #     # homepage.pack()
    # else:
    #     result_label.configure(text="Login Failed")

    login_page.pack_forget()
    homepage.pack(fill="both", expand=True, anchor=CENTER)

# go back to login_page
def go_back():
    homepage.pack_forget()
    login_page.pack(fill="both", expand=True, anchor=CENTER)

def hide_indicators():
    home_indicate.configure(fg_color="grey")
    adopt_indicate.configure(fg_color="grey")
    donate_indicate.configure(fg_color="grey")

def button_event(label, page):
    hide_indicators()
    label.configure(fg_color="red")
    delete_pages()
    page()

def home_page():
    home_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")

    lb = ctk.CTkLabel(home_frame, text="Welcome to Pusaa", font=("Arial", 20))
    lb.pack(padx=10, pady=10)

    home_frame.pack(pady=20)

def adopt_page():
    adopt_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")

    lb = ctk.CTkLabel(adopt_frame, text="Adopt a pet", font=("Arial", 20))
    lb.pack(padx=10, pady=10)

    adopt_frame.pack(pady=20)

def donate_page():
    donate_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")

    lb = ctk.CTkLabel(donate_frame, text="Donate to Pusaa", font=("Arial", 20))
    lb.pack(padx=10, pady=10)

    donate_frame.pack(pady=20)

def delete_pages():
    for widget in main_frame.winfo_children():
        widget.destroy()
    

# Set the default theme for the widgets
# ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create the main window
root = ctk.CTk()
root.title("Login")
# root.geometry("300x300")
root.geometry("500x400") # changed the size of the geometry for the homepage

# Create the first page (login_page)
login_page = ctk.CTkFrame(root)
login_page.pack(fill="both", expand=True, anchor=CENTER)

# Create and place widgets using the place method with anchor "center"
username_label = ctk.CTkLabel(login_page, text="Username:")
username_label.place(relx=0.5, rely=0.25, anchor="center")

username_entry = ctk.CTkEntry(login_page)
username_entry.place(relx=0.5, rely=0.35, anchor="center")

password_label = ctk.CTkLabel(login_page, text="Password:")
password_label.place(relx=0.5, rely=0.45, anchor="center")

password_entry = ctk.CTkEntry(login_page, show="*")  # Passwords are hidden with "*"
password_entry.place(relx=0.5, rely=0.55, anchor="center")

login_button = ctk.CTkButton(login_page, text="Login", command=check_login)
login_button.place(relx=0.5, rely=0.70, anchor="center")

result_label = ctk.CTkLabel(login_page, text="")
result_label.place(relx=0.5, rely=0.80, anchor="center")

# Create the second page (application)
homepage = ctk.CTkFrame(root)

# Open the image file using PIL
logo_icon = ctk.CTkImage(Image.open("logo.png"))
home_icon = ctk.CTkImage(Image.open("home.png"))

# Create the navigation bar inside the homepage
nav_bar = ctk.CTkFrame(homepage, fg_color="grey")

logo_label = ctk.CTkLabel(nav_bar, text=" Pusaa", image=logo_icon, compound="left")
logo_label.pack(padx=10, pady=10)

# Place the widgets inside the navigation bar
home_button = ctk.CTkButton(nav_bar, text="Home", image=home_icon, command=lambda: button_event(home_indicate, home_page))
home_button.pack(padx=10, pady=10)

home_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="grey")
home_indicate.place(x=3, y=50)

adopt_button = ctk.CTkButton(nav_bar, text="Adopt", command=lambda: button_event(adopt_indicate, adopt_page))
adopt_button.pack(padx=10, pady=10)

adopt_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="grey")
adopt_indicate.place(x=3, y=100)

donate_button = ctk.CTkButton(nav_bar, text="Donate", command=lambda: button_event(donate_indicate, donate_page))
donate_button.pack(padx=10, pady=10)

donate_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="grey")
donate_indicate.place(x=3, y=150)


nav_bar.pack(side = ctk.LEFT)
nav_bar.pack_propagate(False)
nav_bar.configure(width=100, height=400, bg_color="grey")

main_frame = ctk.CTkFrame(homepage, corner_radius=0)

# display a default page
button_event(home_indicate, home_page)

main_frame.pack(side = ctk.LEFT)    
main_frame.pack_propagate(False)
main_frame.configure(width=400, height=400)


# Start the main loop
root.mainloop()


