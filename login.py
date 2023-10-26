import customtkinter as ctk
from customtkinter import *
import pandas as pd

# Open the CSV file that will act as the database for the credentials
df = pd.read_csv('credentials.csv')

# Create a list of usernames and passwords from the CSV file
usernames = df['username'].tolist()
passwords = df['password'].tolist()

def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if the username and password entered match the ones in the CSV file
    if entered_username in usernames and entered_password in passwords:
        result_label.configure(text="Login Successful")
        # if successful, hide login_page and display page2
        login_page.pack_forget()
        page2.pack(fill="both", expand=True, anchor=CENTER)
    else:
        result_label.configure(text="Login Failed")

# go back to login_page
def go_back():
    page2.pack_forget()
    login_page.pack(fill="both", expand=True, anchor=CENTER)

# Set the default theme for the widgets
# ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create the main window
root = ctk.CTk()
root.title("Login")
root.geometry("300x300")

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
page2 = ctk.CTkFrame(root)

# Create and place widgets using the grid method
text_label = ctk.CTkLabel(page2, text="This is the second page")
text_label.grid(row=1, column=0, padx=10, pady=10)

button = ctk.CTkButton(page2, text="Go to login page", command=go_back)
button.grid(row=2, column=0, padx=10, pady=10)

# Start the main loop
root.mainloop()
