import tkinter as tk
import customtkinter as ctk
import pandas as pd

# open the csv file that will act as the database for the credentials
df = pd.read_csv('credentials.csv')

# create a list of usernames and passwords from the csv file
usernames = df['username'].tolist()
passwords = df['password'].tolist()

def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # check if the username and password entered match the ones in the csv file
    if entered_username in usernames and entered_password in passwords:
        result_label.config(text="Login Successful")
    else:
        result_label.config(text="Login Failed")

# Create the main window
root = tk.Tk()
root.title("Login App")

# Create and place widgets
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  # Passwords are hidden with "*"
password_entry.pack()

login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
